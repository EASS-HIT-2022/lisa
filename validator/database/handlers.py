from .mongo import MongoDBManager
from datetime import datetime
from decouple import config


DB_NAME = config("DB_NAME")
DB_PORT = int(config("DB_PORT"))
DB_HOST = config("DB_HOST")
EVENTS_COLLECTION_NAME = "events"
MONGODB = MongoDBManager(host=DB_HOST, port=DB_PORT, database_name=DB_NAME)


def get_events():
    return MONGODB.fetch_collection_data(EVENTS_COLLECTION_NAME)


def validate_events():
    for event in get_events():
        new_event = event.copy()
        new_event["active"] = True if datetime.strptime(event["date"], "%Y-%m-%d").date() >= datetime.now().date() else False
        MONGODB.update(EVENTS_COLLECTION_NAME, event, new_event)


