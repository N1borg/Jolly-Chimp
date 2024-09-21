import schedule
import time
from src.website_status import get_website_status

def job_website():
    get_website_status()

# def job_train():
#     get_train_schedule()

# def job_pihole():
#     get_pihole_data()

# Schedule the jobs
schedule.every(1).minutes.do(job_website)
# schedule.every(5).minutes.do(job_train)
# schedule.every(5).minutes.do(job_pihole)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
