from flask_login import UserMixin
from .app import db


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, id=None, email=None, password=None, name=None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
