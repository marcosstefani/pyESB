from app.connectors.db import DatabaseConnector
from app.models.instance import Instance
from app import config_verify

config = config_verify()

instance = Instance(__name__, config['address'], config['port'])
app = instance.initialize()
connection = DatabaseConnector("sqlite:///" + instance.name + ".db")
db = connection.connect(app)
instance.start(app)