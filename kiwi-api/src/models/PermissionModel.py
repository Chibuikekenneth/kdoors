# src/models/PermissionModel.py
from marshmallow import fields, Schema, EXCLUDE
import datetime
from . import db
from . import UserModel
from .UserModel import UserSchema

from sqlalchemy import and_

class PermissionModel(db.Model):
    """
    Permission Model
    """

    # table name
    __tablename__ = 'user_door_permissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    user = db.relationship('UserModel', backref='user_door_permissions')
    door_id = db.Column(db.Integer, db.ForeignKey('doors.id'),nullable=False)
    creation_time = db.Column(db.DateTime)

    # class constructor
    def __init__(self, user_id, door_id):
        """
        Class constructor
        """
        self.user_id = user_id
        self.door_id = door_id
        self.creation_time = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_permission_by_doorid_userid(userid, doorid):
        return PermissionModel.query.filter(and_( PermissionModel.user_id == userid, PermissionModel.door_id==doorid)).first()

    @staticmethod
    def get_permissions_by_doorid(value):
        return PermissionModel.query.filter_by(door_id=value)
    
    @staticmethod
    def get_all_permissions():
        return PermissionModel.query.all()

class PermissionSchema(Schema):
  id = fields.Int(dump_only=True)
  user_id = fields.Int()
  door_id = fields.Int()
  creation_time = fields.DateTime(dump_only=True)
  user = fields.Nested(UserSchema())

  class Meta:
        # Pass EXCLUDE as Meta option to keep marshmallow 2 behavior
        unknown = EXCLUDE
