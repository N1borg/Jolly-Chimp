from fastapi import APIRouter, HTTPException
from typing import Dict
import requests

router = APIRouter()

@router.get("/schedule")
async def get_train_schedule(route: str):
    # Replace with the actual API URL and parameters
    api_url = f"https://api.trains.com/schedule?route={route}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching train schedule")
    return response.json()
