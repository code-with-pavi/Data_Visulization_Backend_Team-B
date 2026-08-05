from flask import Blueprint, jsonify

from services.analytics_service import get_top_targeted_assets

top_assets_bp = Blueprint("top_assets", __name__)


@top_assets_bp.route("/", methods=["GET"])
def top_assets():

    data = get_top_targeted_assets()

    return jsonify({
        "status": "success",
        "count": len(data),
        "top_assets": data
    })