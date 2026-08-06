import re
from datetime import datetime, timedelta

from config import Config
from database.mongodb import get_db

EVENT_SEARCH_FIELDS = (
    "event_id",
    "source_ip",
    "destination_ip",
    "username",
    "event_type",
    "protocol",
    "source_country",
    "destination_country",
    "device_name",
    "asset_name",
    "department",
)
EVENT_SORT_FIELDS = {
    "timestamp",
    "severity",
    "event_type",
    "source_country",
    "risk_score",
    "event_id",
}


def get_collection(collection_name):
    """
    Return all documents from a collection.
    """

    db = get_db()

    data = list(
        db[collection_name].find(
            {},
            {"_id": 0}
        )
    )

    return data


def _date_value(value, end=False):
    """Validate a date/datetime query value and preserve string-based datasets."""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise ValueError("Dates must use ISO-8601 format, for example 2025-08-01.") from exc

    if end and len(value) == 10:
        parsed += timedelta(days=1)
    return parsed.isoformat(sep=" ")


def build_event_filter(
    search=None,
    severity=None,
    event_type=None,
    status=None,
    country=None,
    start_date=None,
    end_date=None,
):
    """Build a bounded MongoDB filter for event search and analytics endpoints."""
    event_filter = {}
    or_groups = []
    if search:
        expression = {"$regex": re.escape(search.strip()), "$options": "i"}
        or_groups.append([{field: expression} for field in EVENT_SEARCH_FIELDS])
    if severity:
        event_filter["severity"] = {"$in": [item.strip() for item in severity.split(",") if item.strip()]}
    if event_type:
        event_filter["event_type"] = {"$in": [item.strip() for item in event_type.split(",") if item.strip()]}
    if status:
        event_filter["event_status"] = {"$in": [item.strip() for item in status.split(",") if item.strip()]}
    if country:
        or_groups.append([
            {"source_country": {"$regex": re.escape(country.strip()), "$options": "i"}},
            {"destination_country": {"$regex": re.escape(country.strip()), "$options": "i"}},
        ])
    if start_date or end_date:
        timestamp_filter = {}
        if start_date:
            timestamp_filter["$gte"] = _date_value(start_date)
        if end_date:
            timestamp_filter["$lt"] = _date_value(end_date, end=True)
        event_filter["timestamp"] = timestamp_filter
    if len(or_groups) == 1:
        event_filter["$or"] = or_groups[0]
    elif or_groups:
        event_filter["$and"] = [{"$or": group} for group in or_groups]
    return event_filter


def search_events(event_filter, page=1, per_page=50, sort_by="timestamp", sort_order="desc"):
    db = get_db()
    page = max(1, int(page))
    per_page = min(max(1, int(per_page)), Config.MAX_PAGE_SIZE)
    sort_by = sort_by if sort_by in EVENT_SORT_FIELDS else "timestamp"
    direction = -1 if sort_order.lower() == "desc" else 1
    cursor = (
        db["security_events"]
        .find(event_filter, {"_id": 0})
        .sort(sort_by, direction)
        .skip((page - 1) * per_page)
        .limit(per_page)
    )
    return list(cursor), db["security_events"].count_documents(event_filter), per_page


def aggregate_events(pipeline):
    return list(get_db()["security_events"].aggregate(pipeline))


def get_assets():

    return get_collection("assets")


def get_vulnerabilities():

    return get_collection("vulnerabilities")


def get_security_events():

    return get_collection("security_events")


def get_incidents():

    return get_collection("incident_history")


def get_threats():

    return get_collection("threat_intelligence")


def get_mitre():

    return get_collection("mitre_mapping")


def get_enriched_events():

    return get_collection("enriched_events")


def get_mapped_events():

    return get_collection("mapped_events")


def get_features():

    return get_collection("engineered_features")


def get_high_risk_assets():
    """
    Return assets with High or Critical risk.
    """

    db = get_db()

    result = list(
        db["engineered_features"].find(
            {
                "risk_category": {
                    "$in": [
                        "High",
                        "Critical"
                    ]
                }
            },
            {"_id": 0}
        )
    )

    return result


def get_dashboard_summary():
    """
    Generate dashboard statistics.
    """

    db = get_db()

    summary = {
        "assets": db["assets"].count_documents({}),
        "vulnerabilities": db["vulnerabilities"].count_documents({}),
        "security_events": db["security_events"].count_documents({}),
        "incidents": db["incident_history"].count_documents({}),
        "threats": db["threat_intelligence"].count_documents({}),
        "mapped_events": db["mapped_events"].count_documents({}),
        "high_risk_assets": db["engineered_features"].count_documents(
            {
                "risk_category": {
                    "$in": [
                        "High",
                        "Critical"
                    ]
                }
            }
        )
    }

    return summary