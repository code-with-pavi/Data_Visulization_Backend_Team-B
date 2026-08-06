# API Documentation

## Core endpoints

GET `/health` or `/api/health` - service and MongoDB health
GET `/api/assets/` - assets
GET `/api/vulnerabilities/` - vulnerabilities
GET `/api/incidents/` - incident history
GET `/api/threats/` - threat intelligence
GET `/api/dashboard/` - dashboard summary

## Add-on endpoints

GET `/api/events` - searchable, filterable, paginated security events.
Supported query parameters: `q`, `severity`, `event_type`, `status`, `country`,
`start_date`, `end_date`, `page`, `per_page`, `sort_by`, and `sort_order`.

GET `/api/events/export.csv` - export the current event filters as CSV.
GET `/api/reports/threats.pdf` - download a live threat analytics PDF report.
GET `/api/analytics/overview` - severity, event type, country, MITRE and user analytics.
GET `/api/analytics/threat-timeline?interval=day|month` - threat activity over time.
GET `/api/analytics/top-targeted-assets?limit=10` - assets with the most events.
GET `/api/analytics/heatmap` - source/destination country event intensity.

The timeline, top-assets and heatmap endpoints also have short aliases:
`/api/threat-timeline`, `/api/top-targeted-assets`, and `/api/heatmap`.

All errors return a consistent JSON body with `status`, `error.code`,
`error.message`, and `error.request_id`. Every request is logged to the
configured log file and includes an `X-Request-ID` response header.

External integrations:
- NVD CVE API: https://services.nvd.nist.gov/rest/json/cves/2.0
- AbuseIPDB API: https://api.abuseipdb.com/api/v2/check

Copy `Backend/.env.example` to `Backend/.env` for local development. Store
production values in environment variables or a secret manager; never commit
credentials to GitHub.
