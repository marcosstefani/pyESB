from app.connectors.db import DatabaseConnector
from app.models.instance import Instance
from app import config_verify
from flask import render_template

config = config_verify()

instance = Instance(__name__, config['address'], config['port'])
app = instance.initialize()
connection = DatabaseConnector("sqlite:///" + instance.name + ".db")
db = connection.connect(app)

@app.route('/')
def index():
    return render_template('index.html')

instance.start(app)
