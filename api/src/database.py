import mysql.connector
import os

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=3306,
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)

def close_db_connection(connection):
    if connection.is_connected():
        connection.close()
