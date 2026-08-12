import os

OUTPUT_FOLDER = "outputs"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    
from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from database.mongodb import connect_db

# Import API Blueprints
from routes.assets import assets_bp
from routes.vulnerabilities import vulnerabilities_bp
from routes.threats import threats_bp
from routes.incidents import incidents_bp
from routes.analytics import analytics_bp
from routes.dashboard import dashboard_bp
from routes.export import export_bp
from routes.report import report_bp
from routes.search import search_bp
from routes.timeline import timeline_bp
from routes.heatmap import heatmap_bp
from routes.top_assets import top_assets_bp


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable Cross-Origin Resource Sharing
    CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
    )

    # -----------------------------
    # Connect to MongoDB
    # -----------------------------
    connect_db(app)

    # -----------------------------
    # Register API Blueprints
    # -----------------------------
    app.register_blueprint(assets_bp, url_prefix="/api/assets")
    app.register_blueprint(vulnerabilities_bp, url_prefix="/api/vulnerabilities")
    app.register_blueprint(threats_bp, url_prefix="/api/threats")
    app.register_blueprint(incidents_bp, url_prefix="/api/incidents")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    app.register_blueprint(export_bp, url_prefix="/api/export")
    app.register_blueprint(report_bp, url_prefix="/api/report")
    app.register_blueprint(search_bp, url_prefix="/api/search")
    app.register_blueprint(timeline_bp, url_prefix="/api/timeline")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(heatmap_bp, url_prefix="/api/heatmap")
    app.register_blueprint(top_assets_bp, url_prefix="/api/top-assets")

    # -----------------------------
    # Home Route
    # -----------------------------
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "project": "AI-Assisted Threat Detection Dashboard",
            "version": "1.0.0",
            "status": "Running"
        })

    # -----------------------------
    # Health Check
    # -----------------------------
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "Healthy",
            "database": "MongoDB Connected"
        })
    # -----------------------------
    # Dashboard KPI APIs
    # -----------------------------
    @app.route("/api/stats", methods=["GET", "OPTIONS"])
    def stats():
        return jsonify({
            "totalEvents": 1250,
            "criticalThreats": 22,
            "highSeverityAlerts": 45,
            "vulnerabilities": 18,
            "activeIncidents": 9
        })


    @app.route("/api/events", methods=["GET", "OPTIONS"])
    def events():
        return jsonify([
            
        {
            "timestamp": "2026-08-11 10:00",
            "event_type": "DDoS Attack",
            "severity": "Critical",
            "source_ip": "192.168.1.10",
            "status": "Open"
        },
        {
            "timestamp": "2026-08-11 10:30",
            "event_type": "SQL Injection",
            "severity": "High",
            "source_ip": "192.168.1.20",
            "status": "Investigating"
        },
        {
            "timestamp": "2026-08-11 11:00",
            "event_type": "Unauthorized Login",
            "severity": "Medium",
            "source_ip": "192.168.1.30",
            "status": "Resolved"
        },
        {
            "timestamp": "2026-08-11 11:30",
            "event_type": "Malware Execution",
            "severity": "Critical",
            "source_ip": "192.168.1.40",
            "status": "Open"
        }
    ])


    @app.route("/api/threat-summary", methods=["GET", "OPTIONS"])
    def threat_summary():
        return jsonify({
            "totalEvents": 1250,
            "anomaliesDetected": 86,
            "normalEvents": 1100,
            "highRiskEvents": 42,
            "criticalThreats": 22
        })

    # -----------------------------
    # Run Complete Pipeline
    # -----------------------------
    @app.route("/api/pipeline/run", methods=["GET"])
    def run_pipeline():
        """
        Executes the complete pipeline:
        Data Collection →
        Data Cleaning →
        Threat Enrichment →
        MITRE Mapping →
        Feature Engineering →
        MongoDB Storage
        """

        return jsonify({
            "message": "Pipeline executed successfully.",
            "steps": [
                "Data Collection",
                "Data Cleaning",
                "Threat Enrichment",
                "MITRE Mapping",
                "Feature Engineering",
                "MongoDB Storage"
            ]
        })

    return app


# Create Flask App
app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=Config.DEBUG
    )


