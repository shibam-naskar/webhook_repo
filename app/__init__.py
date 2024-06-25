from flask import Flask
from .extensions import init_app
from app.webhook.routes import webhook
from app.getrecents.routes import getrecents

def create_app():
    app = Flask(__name__)

    # Initialize extensions
    init_app(app)

    # Register Blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(getrecents)

    return app
