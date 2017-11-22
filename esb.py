from app.connectors.db import DatabaseConnector
from app import Instance

inst1 = Instance("app1", '127.0.0.1', 8080)
app1 = inst1.initialize()
con1 = DatabaseConnector("sqlite:///" + inst1.name + ".db")
db1 = con1.connect(app1)
# inst1.start(app1)

inst2 = Instance("app2", '127.0.0.1', 8081)
app2 = inst2.initialize()
con2 = DatabaseConnector("sqlite:///" + inst2.name + ".db")
db2 = con2.connect(app2)
inst2.start(app2)
