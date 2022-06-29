import pymongo


class MongoDBManager:
    def __init__(self, host, port, database_name):
        self.connection = pymongo.MongoClient(host=host, port=port)
        self.database_name = database_name
        self.database = self.connection[self.database_name]
        self.collections = {}

    def _is_database_exists(self) -> bool:
        return self.database_name in self.connection.list_database_names()

    def _add_collection(self, collection_name: str):
        self.collections[collection_name] = self.database[collection_name]

    def _is_collection_added(self, collection_name: str):
        return collection_name in self.collections

    def _ensure_collection(self, collection_name: str):
        if not self._is_collection_added(collection_name):
            self._add_collection(collection_name)

    def get_raw_collection_data(self, collection_name: str):
        self._ensure_collection(collection_name)
        return self.collections[collection_name].find()

    def fetch_collection_data(self, collection_name: str):
        collection_data = []
        raw_collection_data = self.get_raw_collection_data(collection_name)

        for document in raw_collection_data:
            del document["_id"]
            collection_data.append(document)

        return collection_data

    def update(self, collection_name: str, query: str, new_data: str):
        self._ensure_collection(collection_name)
        new_data = {"$set": new_data}
        test = self.collections[collection_name].update_one(query, new_data)

        print(test)