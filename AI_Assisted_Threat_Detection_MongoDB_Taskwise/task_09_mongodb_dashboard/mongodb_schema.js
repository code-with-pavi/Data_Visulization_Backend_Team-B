// MongoDB database: threat_detection_db
use('threat_detection_db');

db.security_events.createIndex({event_id:1},{unique:true});
db.security_events.createIndex({timestamp:-1});
db.security_events.createIndex({source_ip:1});
db.security_events.createIndex({severity:1});
db.security_events.createIndex({risk_score:-1});

db.threat_intelligence.createIndex({indicator:1},{unique:true});
db.vulnerabilities.createIndex({cve_id:1},{unique:true});
db.assets.createIndex({asset_id:1},{unique:true});
db.incidents.createIndex({incident_id:1},{unique:true});
