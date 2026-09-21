from fastapi import APIRouter , status , Response
from fastapi import Depends
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import userSchemas
from ..services import userServices
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(request: userSchemas.User , db: Session = Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
    return userServices.create_user(request,db)

@router.get('', status_code=status.HTTP_200_OK , response_model=List[userSchemas.UserResponse])
def all_users(db: Session =Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
   return userServices.all_users(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=userSchemas.UserResponse)
def view_user(id:int , response:Response , db: Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
    return userServices.view_user(id,response,db)


@router.put('/{id}' , status_code=status.HTTP_200_OK)
def update(id:int , request: userSchemas.User , db:Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
    return userServices.update_user(id,request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int , db:Session=Depends(get_db),current_user: userSchemas.User= Depends(get_current_user)):
    return userServices.delete_user(id,db)