# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# print(__name__)
# app = Flask(__name__)
# app.config.from_json('../db.json')
# db = SQLAlchemy(app)
# db.create_all()

# print(app)
# print(db)
from flask import Flask

class Instance():
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.debug = True
    
    def initialize(self):
        app = Flask(self.name)

        return app

    def start(self, app):
        app.run(host=self.host, port=self.port, debug=self.debug)
