from pydantic import BaseModel

class UserRequest(BaseModel):
    message : str

class AIResponse(BaseModel):
    message : str