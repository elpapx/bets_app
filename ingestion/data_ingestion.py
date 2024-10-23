import praw
from pymongo import MongoClient
from utils.logger import setup_logger
from utils.exception_utils import handle_exception


class RedditDataIngestion:
    def __init__(self, config):
        self.reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            username=config.username,
            password=config.password,
            user_agent=config.user_agent
        )
        self.mongo_client = MongoClient(config.mongo_uri)
        self.database = self.mongo_client[config.mongo_db_name]
        self.collection = self.database[config.mongo_collection]
        self.logger = setup_logger(__name__)

    @handle_exception
    def fetch_posts(self, subreddit_name: str, limit: int = 10):
        self.logger.info(f"Fetching top {limit} posts from subreddit: {subreddit_name}")
        subreddit = self.reddit.subreddit(subreddit_name)
        top_posts = subreddit.hot(limit=limit)
        dataset = []

        # Extrae los posts y sus comentarios
        for post in top_posts:
            post_data = {
                "id": post.id,
                "title": post.title,
                "score": post.score,
                "url": post.url,
                "num_comments": post.num_comments,
                "created": post.created_utc,
                "body": post.selftext,
                "comments": []
            }

            # Extrae comentarios del post
            post.comments.replace_more(limit=0)  # Para obtener todos los comentarios sin restricciones
            for comment in post.comments.list():
                post_data["comments"].append({
                    "id": comment.id,
                    "body": comment.body,
                    "score": comment.score,
                    "created": comment.created_utc
                })

            # Añadir el post al dataset
            dataset.append(post_data)

        return dataset

    @handle_exception
    def save_to_mongo(self, data):
        self.logger.info(f"Saving {len(data)} posts to MongoDB")
        if data:
            self.collection.insert_many(data)
            self.logger.info("Data successfully saved to MongoDB")
        else:
            self.logger.warning("No data to save")
