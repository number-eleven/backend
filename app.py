from flask import Flask

from api import api_v0

app = Flask(__name__)
app.register_blueprint(api_v0, url_prefix='/api/v0')

if __name__ == '__main__':
    app.run()