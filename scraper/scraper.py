import schedule
import time
from dotenv import load_dotenv
from src.website_status import get_website_status
from src.pihole_status import get_pihole_status

# Load environment variables from .env file
load_dotenv()

def job_website():
    get_website_status()

def job_pihole():
    get_pihole_status()

# Schedule the jobs
schedule.every(1).minutes.do(job_website)
schedule.every(1).minutes.do(job_pihole)

time.sleep(20)

print("Running scheduled jobs...")
get_website_status()
get_pihole_status()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
