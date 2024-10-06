import schedule
import time
from dotenv import load_dotenv
from src.websites_status import get_websites_status
from src.pihole_status import get_pihole_status

# Load environment variables from .env file
load_dotenv()

def job_websites():
    get_websites_status()

def job_pihole():
    get_pihole_status()

# Schedule the jobs
schedule.every(1).minutes.do(job_websites)
schedule.every(1).minutes.do(job_pihole)

time.sleep(20)

print("Running scheduled jobs...")
get_websites_status()
get_pihole_status()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
