# Task 9: MongoDB + Dashboard

Database: `threat_detection_db`

Collections:
- security_events
- threat_intelligence
- vulnerabilities
- assets
- incidents

Run MongoDB locally, then:
`pip install pymongo pandas`
`python import_data.py`

The API can read from MongoDB after replacing CSV reads with collection queries.
