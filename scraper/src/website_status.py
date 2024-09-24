import json
import requests
import mysql.connector
from dotenv import load_dotenv
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()

# Get a connection to the database
def get_db_connection():
    return mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            port=3306,
            database=os.getenv('MYSQL_DATABASE'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD')
        )

# Load the websites from config.json
def load_websites_from_config():
    with open('./config.json', 'r') as f:
        return json.load(f).get('websites', [])

# Check website status
def check_website_status(url):
    try:
        response = requests.get(url, timeout=10)
        return 1 if response.status_code == 200 else 0
    except requests.RequestException:
        return 0

# Insert or update website status in the database
def update_website_status_in_db(name, url, status):
    connection = get_db_connection()
    if connection is None:
        print("Error: Could not connect to the database.")

    cursor = connection.cursor(dictionary=True)

    # Check if the website already exists in the database
    cursor.execute("SELECT * FROM websites WHERE url = %s", (url,))
    website = cursor.fetchone()

    if website:
        # Update existing website status if changed
        if website['status'] != status:
            cursor.execute(
                "UPDATE websites SET status = %s WHERE url = %s",
                (status, url)
            )
            connection.commit()
    else:
        # Insert new website entry if it doesn't exist
        cursor.execute(
            "INSERT INTO websites (name, url, status) VALUES (%s, %s, %s)",
            (name, url, status)
        )
        connection.commit()

    cursor.close()
    connection.close()

# Task to check website status and update the database
def check_and_update_status(site):
    name = site['name']
    url = site['url']
    status = check_website_status(url)
    update_website_status_in_db(name, url, status)

# Get website statuses concurrently and update the database
def get_website_status():
    websites = load_websites_from_config()

    # Use ThreadPoolExecutor to check all websites concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_and_update_status, site) for site in websites]

        # Wait for all threads to complete
        for future in as_completed(futures):
            future.result()  # This will raise any exception if occurred during thread execution
