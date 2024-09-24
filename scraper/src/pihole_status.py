import json
import requests
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Get a connection to the database
def get_db_connection():
    return mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            port=3306,
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )

# Get Pi-hole status and stats
def get_pihole_stats():
    try:
        host = os.getenv("PIHOLE_HOST")
        api_key = os.getenv("PIHOLE_API_KEY")
        response = requests.get(f"http://{host}/admin/api.php?summaryRaw&auth={api_key}", timeout=10)
        data = response.json()

        status = 1 if data['status'] == 'enabled' else 0
        dns_queries_today = data.get('dns_queries_today', 0)
        ads_blocked_today = data.get('ads_blocked_today', 0)
        ads_percentage_today = float(data.get('ads_percentage_today', 0.0))

        return {
            'status': status,
            'dns_queries_today': dns_queries_today,
            'ads_blocked_today': ads_blocked_today,
            'ads_percentage_today': ads_percentage_today
        }
    except Exception as e:
        # Set status to 0 if Pi-hole is not responding
        print(f"Error retrieving Pi-hole data: {e}")
        return {
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
                status = %s,
                dns_queries_today = %s,
                ads_blocked_today = %s,
                ads_percentage_today = %s
            ORDER BY id DESC LIMIT 1;
            """
            values = (
                pihole_data['status'],
                pihole_data['dns_queries_today'],
                pihole_data['ads_blocked_today'],
                pihole_data['ads_percentage_today']
            )

            cursor.execute(sql, values)
        else:
            # Insert new data
            sql = """
            INSERT INTO pihole (status, dns_queries_today, ads_blocked_today, ads_percentage_today)
            VALUES (%s, %s, %s, %s);
            """
            values = (
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
    connection.close()
