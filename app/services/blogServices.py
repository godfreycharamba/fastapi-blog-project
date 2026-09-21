from fastapi import Depends , status , HTTPException , Response
from ..database import get_db
from sqlalchemy.orm import Session , joinedload
from ..models import userModel , blogModel
from ..schemas import blogSchemas, userSchemas

def create_blog(request: blogSchemas.Blog , db: Session):
    new_blog = blogModel.Blog(title=request.title , body=request.body , user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
   
    return new_blog

def all_blogs(db: Session):
    blogs = db.query(blogModel.Blog).all()
    return blogs

def view(id, db:Session):
    blog  = db.query(blogModel.Blog).filter(blogModel.Blog.id==id).first()

    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'details': f'Blog with id {id} not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'Blog with id {id} not found')

    return blog

def update(id ,response: Response, request: blogSchemas.Blog , db: Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id==id)

    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail= f'Blog with id {id} not found')

    blog.update(request.model_dump(exclude_unset=True))
    db.commit()
    
    return blog.first()

def delete_blog(id , db: Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return None