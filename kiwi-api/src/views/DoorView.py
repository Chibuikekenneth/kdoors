#/src/views/DoorView

from flask import request, json, Response, Blueprint
from ..models.DoorModel import DoorModel, DoorSchema
import redis
from datetime import datetime

redis_client = redis.Redis(host='redis', port=6379, db=0)

door_api = Blueprint('door_api', __name__)
door_schema = DoorSchema()

@door_api.route('/', methods=['GET'])
def get_all():
  """
  Get all doors
  """
  doors = DoorModel.get_all_doors()

  # connect to redis cache
  # use sensorId to get the last communication
  # convert unix time to dateTime
  # Append value to door object and return as json

  for door in doors:
      last_communication = redis_client.get('last_opening_ts:'+door.sensor_uuid)
      if(last_communication != None):
          last_communication = datetime.utcfromtimestamp(int(float(last_communication)))
      door.data = last_communication

  ser_doors = door_schema.dump(doors, many=True)
  return custom_response(ser_doors, 200)


@door_api.route('/<int:door_id>', methods=['GET'])
def get_one(door_id):
  """
  Get A Door
  """
  door = DoorModel.get_one_door(door_id)
  last_communication = redis_client.get('last_opening_ts:'+door.sensor_uuid)
  
  if(last_communication != None):
          last_communication = datetime.utcfromtimestamp(int(float(last_communication)))
  door.data = last_communication

  if not door:
    return custom_response({'error': 'door not found'}, 404)
  data = door_schema.dump(door)
  return custom_response(data, 200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
