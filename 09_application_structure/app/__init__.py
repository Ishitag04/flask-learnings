from flask import Flask
from routes.auth import auth_bp     #login blueprint

def createApp():
    app = Flask(__name__)
    app.secret_key="my-secret-key"
    app.register_blueprint(auth_bp)

    return app

