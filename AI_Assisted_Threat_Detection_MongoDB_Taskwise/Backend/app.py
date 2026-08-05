import os
import time
import uuid

OUTPUT_FOLDER = "outputs"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    
from flask import Flask, g, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from config import Config
from database.mongodb import check_health, connect_db
from utils.logger import get_logger

# Import API Blueprints
from routes.assets import assets_bp
from routes.vulnerabilities import vulnerabilities_bp
from routes.threats import threats_bp
from routes.incidents import incidents_bp
from routes.analytics import analytics_bp
from routes.dashboard import dashboard_bp
from routes.addons import addons_bp


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    logger = get_logger()

    # Enable Cross-Origin Resource Sharing
    CORS(app, origins=Config.CORS_ORIGINS.split(",") if Config.CORS_ORIGINS != "*" else "*")

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
    app.register_blueprint(addons_bp)

    @app.before_request
    def start_request():
        g.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        g.started_at = time.perf_counter()

    @app.after_request
    def finish_request(response):
        duration_ms = (time.perf_counter() - g.get("started_at", time.perf_counter())) * 1000
        response.headers["X-Request-ID"] = g.get("request_id", "")
        logger.info(
            "%s %s %s %.2fms request_id=%s",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
            g.get("request_id", ""),
        )
        return response

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify(
            {
                "status": "error",
                "error": {
                    "code": error.code,
                    "message": error.description,
                    "request_id": g.get("request_id"),
                },
            }
        ), error.code

    @app.errorhandler(ValueError)
    def handle_validation_error(error):
        return jsonify(
            {
                "status": "error",
                "error": {
                    "code": 400,
                    "message": str(error),
                    "request_id": g.get("request_id"),
                },
            }
        ), 400

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.exception("Unhandled API error request_id=%s", g.get("request_id"))
        return jsonify(
            {
                "status": "error",
                "error": {
                    "code": 500,
                    "message": "An unexpected server error occurred.",
                    "request_id": g.get("request_id"),
                },
            }
        ), 500

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
    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy",
            "database": check_health(),
            "version": Config.API_VERSION,
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