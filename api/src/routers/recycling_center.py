from fastapi import APIRouter, HTTPException
from typing import Dict
import requests

router = APIRouter()

@router.get("/hours")
async def get_public_trash_hours(location: str):
    # Replace with the actual API URL and parameters
    api_url = f"https://api.trash.com/hours?location={location}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching trash hours")
    return response.json()
