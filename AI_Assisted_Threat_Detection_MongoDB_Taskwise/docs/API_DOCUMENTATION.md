# API Documentation

GET `/api/health` - service health
GET `/api/events?limit=100` - processed security events
GET `/api/summary` - total events, high-risk events, threat matches
GET `/api/analytics/severity` - severity distribution
GET `/api/analytics/mitre` - MITRE ATT&CK technique distribution

External integrations:
- NVD CVE API: https://services.nvd.nist.gov/rest/json/cves/2.0
- AbuseIPDB API: https://api.abuseipdb.com/api/v2/check

Store API keys in `.env`; never commit secrets to GitHub.
