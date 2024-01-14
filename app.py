import os
import pymongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
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



@app.route("/")
@app.route("/get_locations")
def get_locations():
    client = mongo_connect(MONGO_URI)
    collection_name = "locations"
    database_name = "TheJetsettersJournal"
    db = client[database_name]
    collection = db[collection_name]
    documents = list(collection.find())
    names = [document.get('"name"', 'Name not found') for document in documents]

    return render_template("locations.html", names=names)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
