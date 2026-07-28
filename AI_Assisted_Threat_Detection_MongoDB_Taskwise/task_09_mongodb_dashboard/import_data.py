import pandas as pd
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["threat_detection_db"]

files={
"security_events":"../task_07_feature_engineering/feature_engineered_events.csv",
"threat_intelligence":"../task_01_data_collection/threat_intelligence.csv",
"vulnerabilities":"../task_01_data_collection/vulnerability_feed.csv",
"assets":"../task_01_data_collection/assets.csv",
"incidents":"../task_01_data_collection/incident_records.csv"
}
for collection,file in files.items():
    df=pd.read_csv(file)
    records=df.where(pd.notnull(df),None).to_dict("records")
    db[collection].delete_many({})
    if records: db[collection].insert_many(records)
    print(collection, len(records), "documents inserted")
