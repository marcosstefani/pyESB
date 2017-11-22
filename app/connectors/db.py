from flask_sqlalchemy import SQLAlchemy

class DatabaseConnector:
    def __init__(self, uri):
        self.uri = uri
        self.threads = 2
        self.debug = True

    def connect(self, app):
        json_db = {
            "DEBUG": self.debug,
            "SQLALCHEMY_DATABASE_URI": self.uri,
            "SQLALCHEMY_TRACK_MODIFICATIONS": {},
            "THREADS_PER_PAGE": self.threads,
            "CSRF_ENABLED": True,
            "CSRF_SESSION_KEY": "secret",
            "SECRET_KEY": "secret"
            }
        app.config.from_mapping(json_db)
        self.db = SQLAlchemy(app)
        self.db.create_all()

        return self.db