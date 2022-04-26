from app.model import UserLoginSchema, UserSchema, EventSchema
from app.database.mongo import MongoDBManager
from decouple import config


DB_NAME = config("DB_NAME")
DB_PORT = int(config("DB_PORT"))
DB_HOST = config("DB_HOST")
EVENTS_COLLECTION_NAME = "events"
USERS_COLLECTION_NAME = "users"
MONGODB = MongoDBManager(host=DB_HOST, port=DB_PORT, database_name=DB_NAME)


def is_user_exists(data: UserLoginSchema):
    users_documents = MONGODB.fetch_collection_data(USERS_COLLECTION_NAME)

    for document in users_documents:
        user = UserSchema(**document)
        if user.email == data.email and user.password == data.password:
            return True

    return False


def get_events():
    return MONGODB.fetch_collection_data(EVENTS_COLLECTION_NAME)


def create_event(event: EventSchema):
    MONGODB.insert_one_document(EVENTS_COLLECTION_NAME, event.__dict__)


def create_user(user: UserSchema):
    # TODO: hash the user password
    MONGODB.insert_one_document(USERS_COLLECTION_NAME, user.__dict__)
