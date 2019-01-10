from api.v0 import api_v0

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(api_v0, url_prefix='/api/v0')
db = SQLAlchemy(app)
