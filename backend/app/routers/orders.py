# backend/app/routers/orders.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_orders():
    return {"message": "Order list endpoint working!"}
