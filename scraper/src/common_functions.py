import mysql.connector
import os
import socket
import json

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

# Load the websites from config.json
def load_websites_from_config():
    with open('./config.json', 'r') as f:
        return json.load(f).get('websites', [])

def get_ip_by_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error as e:
        ip_address = 'None'
    return ip_address
