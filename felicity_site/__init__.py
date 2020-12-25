
import json
import os
from flask import Flask, url_for

# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'velocity_facility_faculty2020'

config_file = os.path.join(app.root_path, 'static/config', 'media_config.json')
with open(config_file, 'r') as f:
    media_config = json.load(f)

from felicity_site import routes
