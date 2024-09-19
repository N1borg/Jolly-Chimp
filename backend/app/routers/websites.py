from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..database import get_db
from ..models import Website
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[Website])
async def get_websites_status(db: Session = Depends(get_db)):
    websites = db.query(Website).all()
    if not websites:
        raise HTTPException(status_code=404, detail="No websites found")
    return websites
