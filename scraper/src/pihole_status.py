import requests
import os
from src.common_functions import get_db_connection, close_db_connection

# Get Pi-hole status and stats
def get_pihole_stats():
    try:
        host = os.getenv("PIHOLE_HOST")
        api_key = os.getenv("PIHOLE_API_KEY")
        response = requests.get(f"http://{host}/admin/api.php?summaryRaw&auth={api_key}", timeout=10)
        data = response.json()

        name = host
        status = 1 if data['status'] == 'enabled' else 0
        dns_queries_today = data.get('dns_queries_today', 0)
        ads_blocked_today = data.get('ads_blocked_today', 0)
        ads_percentage_today = float(data.get('ads_percentage_today', 0.0))

        return {
            'name': name,
            'status': status,
            'dns_queries_today': dns_queries_today,
            'ads_blocked_today': ads_blocked_today,
            'ads_percentage_today': ads_percentage_today
        }
    except Exception:
        return {
            'name': host,
            'status': 0,
            'dns_queries_today': 0,
            'ads_blocked_today': 0,
            'ads_percentage_today': 0.0
        }

# Insert or update the Pi-hole stats in the database
def get_pihole_status():
    connection = get_db_connection()
    cursor = connection.cursor()

    pihole_data = get_pihole_stats()
    if pihole_data:
        # Check if there is already data in the table
        cursor.execute("SELECT COUNT(*) FROM pihole;")
        exists = cursor.fetchone()[0] > 0

        if exists:
            # Update the last entry
            sql = """
            UPDATE pihole 
            SET 
                name = %s,
                status = %s,
                dns_queries_today = %s,
                ads_blocked_today = %s,
                ads_percentage_today = %s
            ORDER BY id DESC LIMIT 1;
            """
            values = (
                pihole_data['name'],
                pihole_data['status'],
                pihole_data['dns_queries_today'],
                pihole_data['ads_blocked_today'],
                pihole_data['ads_percentage_today']
            )

            cursor.execute(sql, values)
        else:
            # Insert new data
            sql = """
            INSERT INTO pihole (name, status, dns_queries_today, ads_blocked_today, ads_percentage_today)
            VALUES (%s, %s, %s, %s, %s);
            """
            values = (
                pihole_data['name'],
                pihole_data['status'],
                pihole_data['dns_queries_today'],
                pihole_data['ads_blocked_today'],
                pihole_data['ads_percentage_today']
            )

            cursor.execute(sql, values)

        connection.commit()
    else:
        print("No data to update")

    cursor.close()
    close_db_connection(connection)
