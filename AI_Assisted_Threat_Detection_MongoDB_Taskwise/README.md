# AI-Assisted Threat Detection Dashboard
## Infosys Springboard Virtual Internship 7.0

This repository is organized task-wise according to the backend tasks.

### Task-wise folders
1. `task_01_data_collection` - separate source datasets
2. `task_02_schema_normalization` - standard event schema
3. `task_03_data_cleaning` - missing values, duplicates, invalid timestamps
4. `task_04_severity_standardization` - Critical/High/Medium/Low
5. `task_05_threat_intelligence` - threat feed enrichment
6. `task_06_mitre_mapping` - MITRE ATT&CK technique mapping
7. `task_07_feature_engineering` - ML-ready features and risk score
8. `task_08_api` - FastAPI endpoints
9. `task_09_mongodb_dashboard` - MongoDB database, import script and queries

### MongoDB collections
`security_events`, `threat_intelligence`, `vulnerabilities`, `assets`, `incidents`

### Recommended pipeline
Datasets -> Normalize -> Clean -> Standardize -> Enrich -> MITRE Map -> Feature Engineering -> MongoDB -> API -> Dashboard

All datasets are synthetic educational datasets designed for this project. Do not commit real credentials or API keys.
