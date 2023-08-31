from flask import Blueprint
from app.modles import User
from app.db import get_db


bp = Blueprint('api', __name__, url_prefix = '/api')