from fastapi import APIRouter, Depends
from schemas.post_schemas import PostDisplay, PostBase
from sqlalchemy.orm.session import Session
from blog import blog
from db.database import get_db

router = APIRouter(prefix='/post', tags=['posts'])

@router.post('/')
def create_post(request: PostBase, db: Session = Depends(get_db)):
    
    return blog.create_post(db, request)


@router.get('/all')
def get_all(db: Session = Depends(get_db)):
    return blog.get_all_post(db)