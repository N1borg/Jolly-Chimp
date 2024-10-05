from fastapi import FastAPI
from src.routers import websites, pihole
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(websites.router, prefix="/websites", tags=["websites"])
app.include_router(pihole.router, prefix="/pihole", tags=["pihole"])
