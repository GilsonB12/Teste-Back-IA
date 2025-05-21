from .. import mongo
import datetime

def log_request(request_id, user_id, query, result):
    mongo.db.logs.insert_one({
        "request_id": request_id,
        "user_id": user_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
        "query": query,
        "result": result
    })
