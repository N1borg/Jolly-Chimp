import schedule
import time
from src.website_status import get_website_status
from src.pihole_status import get_pihole_status
# from src.train_status import get_train_status

def job_website():
    get_website_status()

def job_pihole():
    get_pihole_status()

# def job_train():
#     get_train_status()

# Schedule the jobs
schedule.every(1).minutes.do(job_website)
schedule.every(1).minutes.do(job_pihole)
# schedule.every(1).minutes.do(job_train)

print("Running scheduled jobs...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
