from flask import Blueprint, jsonify

from services.analytics_service import get_attack_heatmap

heatmap_bp = Blueprint("heatmap", __name__)


@heatmap_bp.route("/", methods=["GET"])
def heatmap():

    data = get_attack_heatmap()

    return jsonify({
        "status": "success",
        "count": len(data),
        "heatmap": data
    })