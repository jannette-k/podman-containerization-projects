from flask import Flask, request, redirect, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os
import time
from pymongo.errors import ServerSelectionTimeoutError
app = Flask(__name__)

# Connect to MongoDB using environment variable
client = MongoClient(os.environ.get("MONGO_URI"))
db = client.todo_db
todos = db.todos

for _ in range(10):
    try:
        client.server_info()
        break
    except ServerSelectionTimeoutError:
        print("Waiting for MongoDB...")
        time.sleep(3)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task and len(task.strip()) > 0:
            todos.insert_one({
                "task": task.strip(),
                "created_at": datetime.utcnow()
            })
        return redirect("/")

    all_todos = list(todos.find().sort("created_at", -1))
    return render_template("index.html", todos=all_todos)

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)