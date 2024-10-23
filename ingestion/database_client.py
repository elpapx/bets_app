rom pymongo import MongoClient
from config.config import Config
from config.logger import setup_logger

class MongoDBClient:
    def __init__(self, config: Config):
        self.logger = setup_logger("MongoDBClient", "logs/mongodb_client.log")
        try:
            self.client = MongoClient(config.mongo_uri)
            self.db = self.client[config.mongo_db_name]
            self.collection = self.db[config.mongo_collection_name]
            self.logger.info("Connected to MongoDB successfully.")
        except Exception as e:
            self.logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    def insert_data(self, data):
        try:
            if isinstance(data, list):
                self.collection.insert_many(data)
            else:
                self.collection.insert_one(data)
            self.logger.info("Data inserted into MongoDB successfully.")
        except Exception as e:
            self.logger.error(f"Failed to insert data into MongoDB: {e}")
            raise
