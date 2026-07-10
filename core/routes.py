from fastapi import APIRouter

from core.llm import ask_ai

from core.schemas import UserRequest,AIResponse

router = APIRouter()

@router.get("/")
def status():
    return {
        "status" : "running"
    }

@router.post("/chat")
def request(request : UserRequest):
    response = ask_ai(request.message)
    return AIResponse(message=response)