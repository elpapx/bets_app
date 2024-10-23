import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Carga las variables del .env

@dataclass
class Config:
    client_id: str = os.getenv("CLIENT_ID")
    client_secret: str = os.getenv("CLIENT_SECRET")
    username: str = os.getenv("USERNAME")
    password: str = os.getenv("PASSWORD")
    user_agent: str = os.getenv("USER_AGENT")
    mongo_uri: str = os.getenv("MONGO_URI")
    mongo_db_name: str = os.getenv("MONGO_DB_NAME")
    mongo_collection_name: str = os.getenv("MONGO_COLLECTION_NAME")

    def validate(self):
        print(f"Client ID: {self.client_id}")  # Para depuración
        print(f"Client Secret: {self.client_secret}")  # Para depuración
        print(f"Username: {self.username}")  # Para depuración
        print(f"Password: {self.password}")  # Para depuración
        print(f"Mongo URI: {self.mongo_uri}")  # Para depuración

        if not all([self.client_id, self.client_secret, self.username, self.user_agent, self.password, self.mongo_uri]):
            raise ValueError("Invalid credentials")