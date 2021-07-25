#/src/views/UserView

from flask import request, json, Response, Blueprint
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()

@user_api.route('/', methods=['GET'])
def get_all():
  """
  Get all users
  """
  users = UserModel.get_all_users()
  ser_users = user_schema.dump(users, many=True)
  return custom_response(ser_users, 200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
