from fastapi import Depends , status , HTTPException , Response
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import userModel
from ..schemas import userSchemas
from ..utils.hashing import Hash



def create_user(request: userSchemas.User , db: Session):
    
    new_user = userModel.User(name= request.name , email= request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def all_users(db: Session):
    users = db.query(userModel.User).all()
    return users

def view_user(id:int , response:Response , db: Session):
    user = db.query(userModel.User).filter(userModel.User.id == id).first()

    if not user:
        
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= f'User with id {id} not found')

    return user

def update_user(id:int , request: userSchemas.User , db:Session):
    user = db.query(userModel.User).filter(userModel.User.id==id)
    
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"User with id {id} not found")
    
    
    user.update(request.model_dump(exclude_unset=True))
    db.commit()
    
    return user.first()

def delete_user(id:int , db:Session):
    user = db.query(userModel.User).filter(userModel.User.id ==id)
    if not user.first():
        raise HTTPException(status_code=404 , detail=f"User with id {id} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return None