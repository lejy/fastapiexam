from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


# 기본값이 directory="templates" 입니다.
templates = Jinja2Templates(directory="templates", auto_reload=True)
user_router = APIRouter()

@user_router.get("/userinfo")
def user_info(request: Request):
    user_data = {
        "name": "홍길동",
        "username": "hong",
        "role": "staff",
        "tasks": ["공지사항", "설정", "로그아웃"],
        "price": 12345.6789
    }
    return templates.TemplateResponse("userinfo.html", {"request": request, "user": user_data })    



