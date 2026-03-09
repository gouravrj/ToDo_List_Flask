from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["todo_db"]
collection = db["todos"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")
    item_id = request.form.get("itemId")
    item_uuid = request.form.get("itemUuid")
    item_hash = request.form.get("itemHash")

    data = {
        "itemName": item_name,
        "itemDescription": item_description,
        "itemId": item_id,
        "itemUuid": item_uuid,
        "itemHash": item_hash
    }

    collection.insert_one(data)

    return "Todo Item Added Successfully"


if __name__ == "__main__":
    app.run(debug=True)