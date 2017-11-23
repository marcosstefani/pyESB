from flask import Flask
from multiprocessing import Process

class Instance():
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.debug = True
    
    def initialize(self):
        app = Flask(self.name)
        return app

    def run(self, app):
        print('Running App ' + self.name)
        app.run(host=self.host, port=self.port, debug=self.debug)

    def start(self, app):
        process = Process(target=self.run, args=(app,))
        process.start()