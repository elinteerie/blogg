from fastapi import FastAPI, APIRouter
from db.database import engine
from db import models
from routers import post


app = FastAPI()
app.include_router(post.router)


@app.get('/')
def hello_world():
    return "hello world"




models.Base.metadata.create_all(bind=engine)


