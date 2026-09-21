from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name:str
    email:str
    password:str

class UserDetails(BaseModel):
    name:str
    email:str   

class UserResponse(BaseModel):
    
    name:str
    email:str 
    blogs: List["Blog"]=[]
    class Config():
        from_attributes = True

class Login(BaseModel):
    username:str
    password:str   

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
          

from .blogSchemas import Blog
UserResponse.model_rebuild()         