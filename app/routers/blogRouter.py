from fastapi import APIRouter , status , Response
from fastapi import Depends
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import blogSchemas, userSchemas
from ..services import blogServices
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="",
    tags=["Blogs"]
)

@router.post('/blog' , status_code=status.HTTP_201_CREATED)
def create_blog(request: blogSchemas.Blog , db: Session= Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
    return blogServices.create_blog(request,db)

@router.get('/blog' , status_code=status.HTTP_200_OK , response_model=List[blogSchemas.BlogResponse] )
def all(db: Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
   return blogServices.all_blogs(db)

@router.get('/blog/{id}' , status_code=status.HTTP_200_OK , response_model=blogSchemas.BlogResponse)
def view(id:int, db:Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
   return blogServices.view(id, db)

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id ,response: Response, request: blogSchemas.Blog , db: Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
  return blogServices.update(id,response,request,db)

@router.delete('/blog/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def destroy(id , db: Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
   return blogServices.delete_blog(id,db)