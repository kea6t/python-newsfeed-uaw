from app.db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(100), nullable = False)
    
    @validates('email')
    def validate_email(self, key, email):
        # Make sure email address contains @ character
        assert '@' in email
        
        return email