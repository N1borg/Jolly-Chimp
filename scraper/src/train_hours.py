import json
import requests
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get a connection to the database
def get_db_connection():
    print()
    return mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            port=3306,
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )

# Load the websites from config.json
def load_websites_from_config():
    with open('./config.json', 'r') as f:
        return json.load(f).get('websites', [])
