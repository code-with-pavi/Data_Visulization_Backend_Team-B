from flask import Blueprint, jsonify

threats_bp = Blueprint("threats", __name__)

@threats_bp.route("/", methods=["GET"])
def threats():
    return jsonify({
        "status": "success",
        "count": 0,
        "data": []
    })