
import json
from flask import Flask, url_for

# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
config_file = 'felicity_site/static/config/media_config.json'
print(config_file)
with open(config_file, 'r') as f:
    media_config = json.load(f)

# app.config['SECRET_KEY'] = 'fbcf9b74745faa8d224628eabba4222b'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

from felicity_site import routes
