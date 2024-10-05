from fastapi import APIRouter, Depends
from src.database import get_db_connection, close_db_connection
router = APIRouter()

@router.get("/")
def get_websites():
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}

    cursor = connection.cursor(dictionary=True)

    # Corrected SQL query with commas between column names
    select_query = """
        SELECT name, ip, status, dns_queries_today, ads_blocked_today, ads_percentage_today 
        FROM pihole
    """
    cursor.execute(select_query)

    result = cursor.fetchall()
    close_db_connection(connection)

    return result
