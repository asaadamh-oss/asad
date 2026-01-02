from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import DevConfig, ProdConfig
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["PDF_OUTPUT_FOLDER"], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    from app import models

    with app.app_context():
        db.create_all()

    from app.routes import main
    app.register_blueprint(main)

    return app
