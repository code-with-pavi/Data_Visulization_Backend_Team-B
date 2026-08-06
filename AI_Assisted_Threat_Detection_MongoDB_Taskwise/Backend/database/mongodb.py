from pymongo import MongoClient
from config import Config

client = None
db = None


def connect_db(app=None):
    """
    Connect to MongoDB.
    """

    global client, db

    client = MongoClient(
        Config.MONGO_URI,
        serverSelectionTimeoutMS=Config.MONGO_SERVER_SELECTION_TIMEOUT_MS,
        connectTimeoutMS=Config.MONGO_CONNECT_TIMEOUT_MS,
    )
    db = client[Config.DATABASE_NAME]

    if app is not None:
        app.logger.info("MongoDB client configured for database '%s'", Config.DATABASE_NAME)


def get_db():
    """
    Return MongoDB database instance.
    """

    if db is None:
        raise RuntimeError("MongoDB is not configured. Call connect_db first.")
    return db


def check_health():
    """Return a small, safe MongoDB health payload without exposing credentials."""
    if client is None or db is None:
        return {"status": "not_configured", "database": Config.DATABASE_NAME}

    try:
        client.admin.command("ping")
        return {"status": "connected", "database": Config.DATABASE_NAME}
    except Exception:
        return {"status": "unavailable", "database": Config.DATABASE_NAME}