import bcrypt
from app.db import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import validates

salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(100), nullable = False)
    is_admin = Column(Boolean, default = False)
    
    @validates('email')
    def validate_email(self, key, email):
        # Make sure email address contains @ character
        assert '@' in email
        
        return email
    
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4
        
        return bcrypt.hashpw(password.encode('utf-8'), salt)