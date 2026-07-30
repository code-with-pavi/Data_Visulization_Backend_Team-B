from pymongo import MongoClient
from config import Config

client = None
db = None


def connect_db(app=None):
    """
    Connect to MongoDB.
    """

    global client, db

    try:
        client = MongoClient(Config.MONGO_URI)

        db = client[Config.DATABASE_NAME]

        print(f"Connected to MongoDB: {Config.DATABASE_NAME}")

    except Exception as e:
        print("MongoDB Connection Error")
        print(e)


def get_db():
    """
    Return MongoDB database instance.
    """

    return db