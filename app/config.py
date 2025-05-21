import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/fabiodb")
    # MONGO_URI = "mongodb://localhost:27017/fabiodb"
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
