from app.models import User
from app.db import Session, Base, engine 

# Drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

