# test.py
# FastAPI의 APIRouter를 사용하여 '/api/hello' 엔드포인트를 만든다.
# 이 엔드포인트는 GET 요청 시 JSON으로 {"message": "Hello from FastAPI!"}를 응답한다.

from fastapi import APIRouter

router = APIRouter()

@router.get("/api/hello")
async def get_hello():
    # 간단한 문자열 메시지를 응답
    return {"message": "Hello from FastAPI!"}
