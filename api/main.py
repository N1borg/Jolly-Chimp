from fastapi import FastAPI
from dotenv import load_dotenv
from src.routers import pihole, websites

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(pihole.router, prefix="/pihole", tags=["pihole"])
app.include_router(websites.router, prefix="/websites", tags=["websites"])
