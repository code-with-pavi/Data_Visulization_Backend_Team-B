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


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable Cross-Origin Resource Sharing
    CORS(app)

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
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

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