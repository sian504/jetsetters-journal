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
    

client = mongo_connect(MONGO_URI)
print('This is it')
print(client)


def download_collection(client, database_name, collection_name):
    db = client[database_name]
    collection = db[collection_name]
    documents = list(collection.find())
    return documents


collection_name = "locations"
database_name = "TheJetsettersJournal"
documents = download_collection(client, database_name, collection_name)
# for document in documents:
print(documents)