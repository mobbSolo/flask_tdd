# create_db.py

from app import db
from models import Flaskr

db.create_all()

db.session.commit()
