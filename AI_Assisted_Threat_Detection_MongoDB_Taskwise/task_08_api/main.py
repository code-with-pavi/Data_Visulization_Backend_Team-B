from fastapi import FastAPI
from pathlib import Path
import pandas as pd
app=FastAPI(title="AI-Assisted Threat Detection API")
DATA=Path("../task_07_feature_engineering/feature_engineered_events.csv")
@app.get("/")
def root(): return {"project":"AI-Assisted Threat Detection Dashboard","database":"MongoDB","status":"running"}
@app.get("/api/health")
def health(): return {"status":"healthy"}
@app.get("/api/events")
def events(limit:int=100):
    return pd.read_csv(DATA).head(limit).to_dict(orient="records")
@app.get("/api/summary")
def summary():
    df=pd.read_csv(DATA)
    return {"total_events":int(len(df)),"high_risk":int((df["risk_score"]>=75).sum()),"threat_matches":int(df["threat_indicator_match"].sum())}
@app.get("/api/analytics/severity")
def severity(): return pd.read_csv(DATA)["severity"].value_counts().to_dict()
@app.get("/api/analytics/mitre")
def mitre(): return pd.read_csv(DATA)["mitre_technique"].value_counts().to_dict()
