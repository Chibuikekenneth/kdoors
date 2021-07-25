#/src/views/PermissionView

from flask import request, g, json, Response, Blueprint
from ..models.PermissionModel import PermissionModel, PermissionSchema

permission_api = Blueprint('permission_api', __name__)
permission_schema = PermissionSchema()

@permission_api.route('/', methods=['GET'])
def get_all():
  """
  Get all permissions
  """
  permissions = PermissionModel.get_all_permissions()
  ser_permissions = permission_schema.dump(permissions, many=True)
  return custom_response(ser_permissions, 200)



@permission_api.route('/<int:door_id>', methods=['GET'])
def get_permissions(door_id):
  """
  Get all permissions by door Id
  """
  permissions = PermissionModel.get_permissions_by_doorid(door_id)
  ser_permissions = permission_schema.dump(permissions, many=True)
  return custom_response(ser_permissions, 200)



@permission_api.route('/create', methods=['POST'])
def create_permission():
  """
  Create permission for a user
  """
  req_data = request.get_json()

  user_id=req_data.get('user_id')
  door_id=req_data.get('door_id')

  # Check if user alrrady has permission to door (sensor)
  user_perm = PermissionModel.get_permission_by_doorid_userid(user_id, door_id)

  if not user_perm:
    permissions = PermissionModel(user_id, door_id)
    permissions.save()
    ser_permissions = permission_schema.dump(permissions)
    return custom_response(ser_permissions, 200)

  message = {'error': 'User already has permission to this door and sensor'}
  return custom_response(message, 400)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
