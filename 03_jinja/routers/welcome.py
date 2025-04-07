from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


# 기본값이 directory="templates" 입니다.
templates = Jinja2Templates(directory="templates", auto_reload=True)
welcome_router = APIRouter()
# 아무것도 받지 않으면 손님이 뜨고, name에 뭔가 값을 전달하면 해당 값이 뜨도록 
@welcome_router.get("/")
@welcome_router.get("/{name}")
def welcome(name: str="손님"):
    """
    걍 json으로 결과확인
    """
    return {"name": name}

@welcome_router.get("/welcome2/{name}") # fastapi가 자체적으로 request 객체를 만들어서 템플릿에 넘깁니다.
def welcome2(request: Request, name: str="손님"):
    return templates.TemplateResponse("welcome.html", {"request":request, "name": name}) # flask의 render_template 메서드처럼 특정 파일로 request와 name을 전달해서 화면을 그립니다.
