from flask import Blueprint, jsonify

from services.analytics_service import get_live_dashboard

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/", methods=["GET"])
def dashboard():

    data = get_live_dashboard()

    return jsonify({

        "status": "success",

        "data": data

    })