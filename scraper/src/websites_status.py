import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.common_functions import get_db_connection, close_db_connection, load_websites_from_config

# Check website status and measure latency
def check_website_status(url):
    try:
        response = requests.get(url, timeout=10)
        latency = response.elapsed.total_seconds() * 1000
        status = 1 if response.status_code in range(200, 400) else 0
        return status, latency
    except requests.RequestException:
        return 0, 0

# Insert or update website status and latency in the database
def update_website_status_in_db(name, url, status, latency):
    connection = get_db_connection()
    if connection is None:
        print("Error: Could not connect to the database.")
        return

    cursor = connection.cursor(dictionary=True)

    # Check if the website already exists in the database
    cursor.execute("SELECT * FROM websites WHERE url = %s", (url,))
    website = cursor.fetchone()

    if website:
        # Update existing website status and latency if changed
        if website['status'] != status or website['latency'] != latency:
            cursor.execute(
                "UPDATE websites SET status = %s, latency = %s WHERE url = %s",
                (status, latency, url)
            )
            connection.commit()
    else:
        # Insert new website entry if it doesn't exist
        cursor.execute(
            "INSERT INTO websites (name, url, status, latency) VALUES (%s, %s, %s, %s)",
            (name, url, status, latency)
        )
        connection.commit()

    cursor.close()
    close_db_connection(connection)

# Task to check website status and update the database
def check_and_update_status(site):
    name = site['name']
    url = site['url']
    status, latency = check_website_status(url)
    update_website_status_in_db(name, url, status, latency)

# Get website statuses concurrently and update the database
def get_websites_status():
    websites = load_websites_from_config()

    # Use ThreadPoolExecutor to check all websites concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_and_update_status, site) for site in websites]

        # Wait for all threads to complete
        for future in as_completed(futures):
            future.result()  # This will raise any exception if occurred during thread execution
