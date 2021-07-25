# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db

class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    creation_time = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.email = data.get('email')
        self.first_name = data.get('firstname')
        self.last_name = data.get('lastname')
        self.creation_time = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return UserModel.query.all()

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  email = fields.Email(required=True)
  first_name = fields.Str(required=True)
  last_name = fields.Str(required=True)
  creation_time = fields.DateTime(dump_only=True)