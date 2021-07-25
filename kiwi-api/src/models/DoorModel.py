# src/models/DoorModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import AddressModel
from .AddressModel import AddressSchema

class DoorModel(db.Model):
    """
    Door Model
    """

    # table name
    __tablename__ = 'doors'

    id = db.Column(db.Integer, primary_key=True)
    sensor_uuid = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    address = db.relationship('AddressModel', backref='doors')
    installation_time = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.sensor_uuid = data.get('sensor_uuid')
        self.name = data.get('name')
        self.address_id = data.get('address_id')
        self.installation_time = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_doors():
        return DoorModel.query.all()

    @staticmethod
    def get_one_door(id):
        return DoorModel.query.get(id)

class DoorSchema(Schema):
  id = fields.Int(dump_only=True)
  sensor_uuid = fields.Str(required=True)
  name = fields.Str(required=True)
  address_id = fields.Int(required=True)
  address = fields.Nested(AddressSchema())
  installation_time = fields.DateTime(dump_only=True)
  last_communication_time = fields.Method("get_data")

  def get_data(self, obj):
        if hasattr(obj, "data"):
            return obj.data
        return None
        