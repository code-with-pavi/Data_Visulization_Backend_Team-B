# AI-Assisted Threat Detection Dashboard

## Overview

The **AI-Assisted Threat Detection Dashboard** is a cybersecurity analytics platform designed to automate the collection, processing, enrichment, storage, and visualization of security-related data. The system integrates multiple cybersecurity datasets, enriches threat intelligence, maps attacks to the MITRE ATT&CK framework, performs feature engineering, stores processed data in MongoDB, and provides RESTful APIs for a frontend dashboard.

The project enables security analysts to monitor assets, vulnerabilities, security events, and incidents while providing actionable insights through analytics and reporting.

---

# Features

## Core Pipeline

* Data Collection
* Data Cleaning
* Threat Enrichment
* MITRE ATT&CK Mapping
* Feature Engineering
* MongoDB Storage
* REST APIs

---

## Dashboard Features

* Dashboard Analytics
* Search Security Events
* Threat Timeline
* Heatmap of Attacks
* Top Targeted Assets
* Auto Refresh Dashboard API
* Export Security Events as CSV
* Download Threat Report as PDF

---

# Technology Stack

## Backend

* Python 3.10+
* Flask
* Flask-CORS
* Pandas
* NumPy
* PyMongo
* ReportLab

## Database

* MongoDB

## Data Processing

* Pandas
* NumPy

## Logging

* Python Logging Module

---

# Project Structure

```text
backend/
│
├── app.py
├── config.py
├── requirements.txt
│
├── data/
│   ├── assets.csv
│   ├── vulnerabilities.csv
│   ├── security_events.csv
│   ├── incident_history.csv
│   ├── threat_intelligence.csv
│   └── mitre_attack_mapping.csv
│
├── preprocessing/
│   ├── __init__.py
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── threat_enrichment.py
│   ├── mitre_mapping.py
│   └── feature_engineering.py
│
├── database/
│   ├── __init__.py
│   ├── mongodb.py
│   ├── insert_data.py
│   └── queries.py
│
├── models/
│   ├── __init__.py
│   ├── asset_model.py
│   ├── vulnerability_model.py
│   ├── threat_model.py
│   ├── security_event_model.py
│   ├── incident_model.py
│   └── mitre_model.py
│
├── services/
│   ├── __init__.py
│   ├── pipeline_service.py
│   ├── enrichment_service.py
│   ├── mitre_service.py
│   ├── analytics_service.py
│   ├── feature_service.py
│   └── report_service.py
│
├── routes/
│   ├── __init__.py
│   ├── assets.py
│   ├── vulnerabilities.py
│   ├── threats.py
│   ├── incidents.py
│   ├── analytics.py
│   ├── dashboard.py
│   ├── export.py
│   ├── report.py
│   ├── search.py
│   ├── timeline.py
│   ├── heatmap.py
│   └── top_assets.py
│
├── utils/
│   ├── __init__.py
│   ├── constants.py
│   ├── helper.py
│   ├── logger.py
│   └── validators.py
│
├── outputs/
│   ├── cleaned_data.csv
│   ├── enriched_data.csv
│   ├── mapped_data.csv
│   ├── engineered_features.csv
│   └── Threat_Report.pdf
│
└── logs/
    └── application.log
```

---

# Data Processing Pipeline

```text
CSV Datasets
      │
      ▼
Data Collection
      │
      ▼
Data Cleaning
      │
      ▼
Threat Enrichment
      │
      ▼
MITRE ATT&CK Mapping
      │
      ▼
Feature Engineering
      │
      ▼
MongoDB Database
      │
      ▼
REST APIs
      │
      ▼
Threat Detection Dashboard
```

---

# Pipeline Description

## 1. Data Collection

Loads cybersecurity datasets from the `data` folder, including:

* Assets
* Vulnerabilities
* Security Events
* Incident History
* Threat Intelligence
* MITRE ATT&CK Mapping

---

## 2. Data Cleaning

Performs:

* Remove duplicate records
* Handle missing values
* Standardize column names
* Normalize severity levels
* Convert date/time fields
* Remove duplicate columns

Output:

* `outputs/cleaned_data.csv`

---

## 3. Threat Enrichment

Enhances security events by merging:

* Vulnerability information
* Threat intelligence

Generates:

* Threat Score
* Risk Level
* IOC Match
* Known Exploit
* Enrichment Status

Output:

* `outputs/enriched_data.csv`

---

## 4. MITRE ATT&CK Mapping

Maps attacks to the MITRE ATT&CK framework.

Generated fields:

* Technique ID
* Technique Name
* Tactic
* Mapping Status

Output:

* `outputs/mapped_data.csv`

---

## 5. Feature Engineering

Creates analytical features such as:

* Threat Score
* CVSS Score
* Incident Frequency
* Historical Risk
* Asset Risk Score
* Overall Risk Score
* Risk Category

Output:

* `outputs/engineered_features.csv`

---

# MongoDB Collections

The processed datasets are stored in MongoDB collections:

* assets
* vulnerabilities
* security_events
* incident_history
* threat_intelligence
* mitre_mapping
* enriched_events
* mapped_events
* engineered_features

---

# REST API Endpoints

| Method | Endpoint               | Description                   |
| ------ | ---------------------- | ----------------------------- |
| GET    | `/`                    | Home                          |
| GET    | `/health`              | Health Check                  |
| GET    | `/api/assets`          | Retrieve Assets               |
| GET    | `/api/vulnerabilities` | Retrieve Vulnerabilities      |
| GET    | `/api/threats`         | Retrieve Threat Intelligence  |
| GET    | `/api/incidents`       | Retrieve Incidents            |
| GET    | `/api/dashboard`       | Dashboard Statistics          |
| GET    | `/api/analytics`       | Analytics Data                |
| GET    | `/api/export/csv`      | Export Security Events as CSV |
| GET    | `/api/report/pdf`      | Download Threat Report (PDF)  |
| GET    | `/api/search?q=value`  | Search Security Events        |
| GET    | `/api/timeline`        | Threat Timeline               |
| GET    | `/api/heatmap`         | Heatmap Data                  |
| GET    | `/api/top-assets`      | Top Targeted Assets           |

---

# Dashboard Features

## Search Event

Searches security events by:

* Event ID
* Asset ID
* Attack Name
* Severity
* Risk Level
* Status

---

## Threat Timeline

Returns security events sorted by timestamp for chronological visualization.

---

## Heatmap of Attacks

Provides aggregated attack counts grouped by asset (or by location if geographic data is available).

---

## Top Targeted Assets

Returns the assets with the highest number of recorded attacks.

---

## Auto Refresh Dashboard

The dashboard API always returns the latest MongoDB data. The frontend can periodically request `/api/dashboard` to refresh the displayed information.

---

## Export CSV

Downloads all security events as a CSV file.

Generated file:

* `security_events.csv`

---

## Download PDF Report

Generates a PDF report summarizing dashboard statistics and threat information.

Generated file:

* `outputs/Threat_Report.pdf`

---

# Logging

Application logs are stored in:

```text
logs/application.log
```

Logs include:

* Application startup
* MongoDB connection
* Data processing stages
* API requests
* Errors and exceptions

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# MongoDB Configuration

Update `config.py`:

```python
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "ThreatDetectionDB"
```

Ensure the MongoDB server is running before starting the application.

---

# Running the Project

Start the Flask application:

```bash
python app.py
```

Server URL:

```text
http://127.0.0.1:5000
```

---

# Testing APIs

| Feature      | Endpoint                     |
| ------------ | ---------------------------- |
| Home         | `GET /`                      |
| Health       | `GET /health`                |
| Dashboard    | `GET /api/dashboard`         |
| Export CSV   | `GET /api/export/csv`        |
| Download PDF | `GET /api/report/pdf`        |
| Search       | `GET /api/search?q=critical` |
| Timeline     | `GET /api/timeline`          |
| Heatmap      | `GET /api/heatmap`           |
| Top Assets   | `GET /api/top-assets`        |

These endpoints can be tested using a browser (for downloads), Postman, or any REST client.

---

# Output Files

The pipeline generates:

* `outputs/cleaned_data.csv`
* `outputs/enriched_data.csv`
* `outputs/mapped_data.csv`
* `outputs/engineered_features.csv`
* `outputs/Threat_Report.pdf`

---

# Learning Outcomes

This project demonstrates practical implementation of:

* Cybersecurity Data Analytics
* Threat Intelligence Processing
* MITRE ATT&CK Integration
* Feature Engineering
* MongoDB Database Design
* Flask REST API Development
* Data Processing Pipelines
* Backend Architecture
* Dashboard Data Services
* Reporting and Data Export

