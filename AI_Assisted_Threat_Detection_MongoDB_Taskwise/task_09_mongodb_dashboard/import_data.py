import pandas as pd
from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / "Backend" / ".env")

client = MongoClient(
    os.getenv("MONGO_URI", "mongodb://localhost:27017/")
)
db = client[os.getenv("DATABASE_NAME", "ThreatDetectionDB")]

files={
"security_events": PROJECT_ROOT / "task_07_feature_engineering" / "feature_engineered_events.csv",
"threat_intelligence": PROJECT_ROOT / "task_01_data_collection" / "threat_intelligence.csv",
"vulnerabilities": PROJECT_ROOT / "task_01_data_collection" / "vulnerability_feed.csv",
"assets": PROJECT_ROOT / "task_01_data_collection" / "assets.csv",
"incidents": PROJECT_ROOT / "task_01_data_collection" / "incident_records.csv",
}
for collection,file in files.items():
    df=pd.read_csv(file)
    records=df.where(pd.notnull(df),None).to_dict("records")
    db[collection].delete_many({})
    if records: db[collection].insert_many(records)
    print(collection, len(records), "documents inserted")
