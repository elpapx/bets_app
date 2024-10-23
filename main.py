import sys
from config.config import Config
from ingestion.data_ingestion import RedditDataIngestion
from ingestion.database_client import MongoDBClient
from processing.data_transformer import DataTransformer

def main():
    config = Config()
    config.validate()

    if len(sys.argv) < 2:
        print("Usage: python main.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]

    # Ingestión de datos
    data_ingestion = RedditDataIngestion(config)
    posts = data_ingestion.fetch_posts(subreddit_name)

    # Transformar datos
    transformer = DataTransformer()
    transformed_data = transformer.transform(posts)

    # Guardar en MongoDB
    mongo_client = MongoDBClient(config)
    mongo_client.insert_data(transformed_data)

if __name__ == "__main__":
    main()

