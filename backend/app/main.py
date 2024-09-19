from fastapi import FastAPI
from dotenv import load_dotenv
from .routers import websites, pihole, trains, public_trash

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(websites.router, prefix="/websites", tags=["websites"])
app.include_router(pihole.router, prefix="/pihole", tags=["pihole"])
app.include_router(trains.router, prefix="/trains", tags=["trains"])
app.include_router(public_trash.router, prefix="/public-trash", tags=["public-trash"])
