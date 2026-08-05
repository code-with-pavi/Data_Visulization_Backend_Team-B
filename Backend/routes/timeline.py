from flask import Blueprint, jsonify

from database.queries import get_threat_timeline

timeline_bp = Blueprint("timeline", __name__)


@timeline_bp.route("/", methods=["GET"])
def timeline():

    data = get_threat_timeline()

    return jsonify({
        "status": "success",
        "count": len(data),
        "timeline": data
    })