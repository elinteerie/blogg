from sqlalchemy.orm.session import Session
from db.models import Post
from schemas.post_schemas import PostBase, PostDisplay
import datetime


def create_post(db: Session, request: PostBase):
    new_post = Post(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "status_code": "200",
        "post": new_post
    }


def get_all_post(db: Session):
    all_post = db.query(Post).all()
    return all_post