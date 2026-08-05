from flask import Blueprint, request, jsonify

from database.queries import search_security_events

search_bp = Blueprint("search", __name__)


@search_bp.route("/", methods=["GET"])
def search_event():

    keyword = request.args.get("q", "").strip()

    if keyword == "":
        return jsonify({
            "status": "error",
            "message": "Search keyword is required."
        }), 400

    results = search_security_events(keyword)

    return jsonify({
        "status": "success",
        "count": len(results),
        "data": results
    })