import sys
from flask import Blueprint, request
from app.models import User
from app.db import get_db


bp = Blueprint('api', __name__, url_prefix = '/api')

@bp.route('/users', methods = ['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    
    # Create a new user
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )
    
    # Save in database
    print(data)
    return ''