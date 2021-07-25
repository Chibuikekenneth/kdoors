# src/models/AddressModel.py
from marshmallow import fields, Schema
import datetime
from . import db

class AddressModel(db.Model):
    """
    Address Model
    """

    # table name
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128), unique=True, nullable=False)
    postal_code = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    country_code = db.Column(db.String(128), nullable=False)
    geolocation = db.Column(db.Integer, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.street = data.get('street')
        self.postal_code = data.get('postal_code')
        self.city = data.get('city')
        self.state = data.get('state')
        self.country_code = data.get('country_code')
        self.geolocation = data.get('geolocation')
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_address():
        return AddressModel.query.all()

    @staticmethod
    def get_one_address(id):
        return AddressModel.query.get(id)

class AddressSchema(Schema):
  id = fields.Int(dump_only=True)
  street = fields.Str(required=True)
  postal_code = fields.Str(required=True)
  city = fields.Str(required=True)
  state = fields.Str(required=True)
  country_code = fields.Str(required=True)
  geolocation = fields.Str(required=True)
