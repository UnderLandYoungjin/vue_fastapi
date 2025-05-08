# backend/app/routers/users.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users():
    return {"message": "User list endpoint working!"}
