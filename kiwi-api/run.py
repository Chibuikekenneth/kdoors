# /run.py
import os
from flask import Flask

from flask_cors import CORS

from src.models import db
from src.config import app_config

# import api blueprint
from src.views.UserView import user_api as user_blueprint
from src.views.DoorView import door_api as door_blueprint
from src.views.PermissionView import permission_api as permission_blueprint

env_name = os.getenv('FLASK_ENV')

# app initiliazation
app = Flask(__name__)

CORS(app)

app.config.from_object(app_config[env_name])

# initializing db
db.init_app(app)

app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(door_blueprint, url_prefix='/api/v1/doors')
app.register_blueprint(permission_blueprint, url_prefix='/api/v1/permissions')

@app.route('/', methods=['GET'])
def index():
  """
  example endpoint
  """
  return 'Hello Kiwi !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
