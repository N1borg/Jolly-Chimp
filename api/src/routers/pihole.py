from fastapi import APIRouter, HTTPException
from typing import Dict
import requests
import os

router = APIRouter()

@router.get("/stats")
async def get_pihole_stats():
    api_key = os.getenv("PIHOLE_API_KEY")
    url = f"http://pi.hole/admin/api.php?summaryRaw&auth={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching Pi-hole data")
    return response.json()
