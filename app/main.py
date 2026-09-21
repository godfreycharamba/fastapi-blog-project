from fastapi import FastAPI 

from .database import engine ,Base
from .routers import blogRouter , userRouter , authRouter




app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authRouter.router)
app.include_router(blogRouter.router)
app.include_router(userRouter.router)






















