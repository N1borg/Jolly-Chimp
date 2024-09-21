from fastapi import FastAPI
from dotenv import load_dotenv
from src.routers import websites, pihole, trains, recycling_center

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(websites.router, prefix="/websites", tags=["websites"])
app.include_router(pihole.router, prefix="/pihole", tags=["pihole"])
app.include_router(trains.router, prefix="/trains", tags=["trains"])
app.include_router(recycling_center.router, prefix="/recycling-center", tags=["recycling-center"])
