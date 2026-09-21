from ..database import Base
from sqlalchemy import Integer , String , Column , Text , ForeignKey
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(255))    
    email = Column(String(255))
    password = Column(String(255))
    blogs = relationship("Blog" , back_populates="creator")