import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MEDIA_ROOT = os.path.join(basedir, "media")
    UPLOAD_FOLDER = os.path.join(MEDIA_ROOT, "uploads")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB
    WTF_CSRF_ENABLED = True

    # WeasyPrint settings (HTML to PDF)
    PDF_OUTPUT_FOLDER = os.path.join(MEDIA_ROOT, "pdfs")

    # For Bootstrap and UI language
    APP_LANG = "ar"
    APP_DIR = "rtl"

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False