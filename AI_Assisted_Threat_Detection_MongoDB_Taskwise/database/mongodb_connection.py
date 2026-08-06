from pymongo import MongoClient
import os

MONGO_URI=os.getenv("MONGO_URI","mongodb://localhost:27017/")
client=MongoClient(MONGO_URI)
db=client["threat_detection_db"]

security_events=db["security_events"]
threat_intelligence=db["threat_intelligence"]
vulnerabilities=db["vulnerabilities"]
assets=db["assets"]
incidents=db["incidents"]

def insert_events(records):
    if records:
        return security_events.insert_many(records, ordered=False)
    return None
