import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")             


def mongo_connect(url):
    print("Attempting to connect to MongoDB")
    try:
        conn = pymongo.MongoClient(url)
        print("MongoDB is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None


print("Before calling mongo_connect")
client = mongo_connect(MONGO_URI)
print("After calling mongo_connect")


