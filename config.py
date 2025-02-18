import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://neondb_owner:yuB3ZoEa8ptz@ep-small-truth-a5ihn91n-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = "your_secret_key"
