from .database import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True )
    title = Column(String)
    image_url = Column(String)
    content = Column(String)
    creator  = Column(String)
    timestamp = Column(DateTime)
    