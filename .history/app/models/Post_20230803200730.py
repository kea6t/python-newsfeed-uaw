from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    vote_count = column_property(
        select(func.count(Vote.id)).where(Vote.post_id == id).scalar_subquery()
    )
    votes = relationship("Vote", cascade="all,delete")
    
    
    # Inside the vote_count method, we use SQLAlchemy's func.count(Vote.id) to count the number of votes. 
    # The Vote.id is a reference to the id column in the Vote table.
    # We add a filter to the count function, filter(Vote.post_id == self.id). 
    # This filter ensures that we only count the votes that are associated with the current Post instance. 
    # The self.id refers to the id of the current post.
    # By using the @column_property decorator, we are telling SQLAlchemy to treat this method as a column in the database table. 
    # It allows us to access the vote count as if it were a regular attribute of the Post class.
    # @column_property
    # def vote_count(self):
    #     return func.count(Vote.id).filter(Vote.post_id == self.id)

    comments = relationship("Comment", cascade="all,delete")

    user = relationship("User")