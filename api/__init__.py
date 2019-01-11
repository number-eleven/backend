from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.v0 import api_v0

app = Flask(__name__)
app.register_blueprint(api_v0, url_prefix='/api/v0')
db = SQLAlchemy(app)
