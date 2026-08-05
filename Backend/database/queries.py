from database.mongodb import get_db
from database.mongodb import db
from database.mongodb import db
from database.mongodb import db
from database.mongodb import db
from database.mongodb import db
from database.mongodb import db
from database.mongodb import db


def get_top_targeted_assets_data(limit=10):
    """
    Return the most targeted assets.
    """

    pipeline = [

        {
            "$group": {
                "_id": "$asset_id",
                "attack_count": {"$sum": 1},
                "highest_severity": {"$max": "$severity"}
            }
        },

        {
            "$sort": {
                "attack_count": -1
            }
        },

        {
            "$limit": limit
        },

        {
            "$project": {
                "_id": 0,
                "asset_id": "$_id",
                "attack_count": 1,
                "highest_severity": 1
            }
        }

    ]

    return list(
        db.security_events.aggregate(pipeline)
    )


def get_attack_heatmap_data():
    """
    Aggregate attack counts grouped by asset.
    """

    pipeline = [
        {
            "$group": {
                "_id": "$asset_id",
                "attack_count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "asset_id": "$_id",
                "attack_count": 1
            }
        },
        {
            "$sort": {
                "attack_count": -1
            }
        }
    ]

    return list(
        db.security_events.aggregate(pipeline)
    )


def get_live_dashboard_data():
    """
    Return the latest dashboard statistics.
    """

    return {

        "total_assets":
        db.assets.count_documents({}),

        "total_vulnerabilities":
        db.vulnerabilities.count_documents({}),

        "total_security_events":
        db.security_events.count_documents({}),

        "total_incidents":
        db.incident_history.count_documents({}),

        "critical_events":
        db.security_events.count_documents(
            {"severity": "Critical"}
        ),

        "high_events":
        db.security_events.count_documents(
            {"severity": "High"}
        ),

        "last_updated":
        str(db.security_events.find_one(
            sort=[("timestamp", -1)]
        )["timestamp"])
        if db.security_events.count_documents({}) > 0
        else "No Data"
    }


def get_threat_timeline():
    """
    Return security events ordered by timestamp.
    """

    events = list(
        db.security_events.find(
            {},
            {
                "_id": 0,
                "event_id": 1,
                "timestamp": 1,
                "attack_name": 1,
                "severity": 1,
                "risk_level": 1,
                "asset_id": 1
            }
        ).sort("timestamp", 1)
    )

    return events


def search_security_events(keyword):
    """
    Search security events by multiple fields.
    """

    query = {
        "$or": [

            {"event_id": {"$regex": keyword, "$options": "i"}},

            {"asset_id": {"$regex": keyword, "$options": "i"}},

            {"attack_name": {"$regex": keyword, "$options": "i"}},

            {"severity": {"$regex": keyword, "$options": "i"}},

            {"risk_level": {"$regex": keyword, "$options": "i"}},

            {"status": {"$regex": keyword, "$options": "i"}}
        ]
    }

    events = list(
        db.security_events.find(query)
    )

    for event in events:

        event["_id"] = str(event["_id"])

    return events


def get_dashboard_summary():

    return {

        "Total Assets":
        db.assets.count_documents({}),

        "Total Vulnerabilities":
        db.vulnerabilities.count_documents({}),

        "Security Events":
        db.security_events.count_documents({}),

        "Threat Intelligence":
        db.threat_intelligence.count_documents({}),

        "MITRE Mappings":
        db.mitre_mapping.count_documents({}),

        "Engineered Features":
        db.engineered_features.count_documents({})
    }


def get_all_security_events():
    """
    Retrieve all security events from MongoDB.
    """

    collection = db["security_events"]

    data = list(collection.find())

    return data


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