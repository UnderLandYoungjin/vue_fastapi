# backend/app/main.py

from fastapi import FastAPI
from app.routers import users, orders, chat, test  # test 라우터 추가
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 기존 라우터들 유지
app.include_router(users.router, prefix="/users")
app.include_router(orders.router, prefix="/orders")
app.include_router(chat.router, prefix="/chat")

#개발 서버의 요청을 허용하도록 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ['http://localhost:5173']
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 테스트용 라우터 추가
app.include_router(test.router)  # '/api/hello' 그대로 연결

@app.get("/")
def root():
    return {"message": "Backend is running!"}
