from fastapi import APIRouter , Depends , HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import userSchemas
from ..database import get_db
from sqlalchemy.orm import Session 
from ..models import userModel
from ..utils.hashing import Hash
from .. import token

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

   
    access_token = token.create_access_token(
        data={"sub": user.email})
    # return {"data":{"user": {"name": user.name,"email": user.email},
    #         "access_token":access_token,
    #         "token_type":"bearer"}}
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    