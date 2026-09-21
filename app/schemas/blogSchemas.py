from pydantic import BaseModel


class BlogBase(BaseModel):
    title:str
    body:str
    
class Blog(BlogBase):
    class Config():
        from_attributes = True

class BlogResponse(BaseModel):
   
    title:str
    body:str
    creator:"UserDetails"

    class Config():
        from_attributes = True 

from .userSchemas import UserDetails                 
BlogResponse.model_rebuild()