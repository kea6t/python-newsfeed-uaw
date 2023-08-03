from app.models import User
from app.db import Session, Base, engine 

# Drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# Insert users
db.add_all([
    User(username='alesmonde', email='nwestnedge0@cbc.com', password='password123'),
    User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4weather.com', password='password123'),
])

db.commit()

db.close()