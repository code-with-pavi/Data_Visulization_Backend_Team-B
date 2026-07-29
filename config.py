import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    """
    Application Configuration
    """

    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "threat_detection_secret_key")

    # MongoDB Settings
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "ThreatDetectionDB"
    )

    # Debug Mode
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    # API Settings
    API_TITLE = "AI-Assisted Threat Detection Dashboard"
    API_VERSION = "1.0.0"

    # Upload Folder (Optional)
    UPLOAD_FOLDER = "data"

    # Allowed File Extensions
    ALLOWED_EXTENSIONS = {"csv"}

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024