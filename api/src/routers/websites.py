from fastapi import APIRouter, Depends
from src.database import get_db_connection, close_db_connection
router = APIRouter()

@router.get("/")
def get_websites():
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}
   
    cursor = connection.cursor(dictionary=True)

    select_query = "SELECT name, url, status FROM websites"
    cursor.execute(select_query)

    result = cursor.fetchall()
    close_db_connection(connection)

    return result
