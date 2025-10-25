# 📝 Flask + MongoDB Todo App (Podman Compose)

A lightweight, containerized todo list application built with Flask and MongoDB, orchestrated using Podman Compose. This project demonstrates how to build a simple web app with persistent data storage, environment configuration, and container networking.


## 🚀 Project Overview

- **Frontend**: HTML rendered via Flask templates  
- **Backend**: Flask (Python)  
- **Database**: MongoDB  
- **Containerization**: Podman Compose  
- **Persistence**: Named volumes for MongoDB data  


## ⚙️ Setup Instructions

1. Clone the repository and navigate to the root folder.
2. Ensure your `.env` file contains:

   ```env
   FLASK_ENV=development
   MONGO_URI=mongodb://db:27017/todo_db

## Build and Run The Container
podman-compose --env-file .env up --build --security-opt label=disable


📦 Why We Used Volumes (Not Bind Mounts)
We chose named volumes for MongoDB because:

They persist data across container rebuilds and restarts.

They are managed by Podman and isolated from host filesystem changes.

They avoid permission issues common with bind mounts on Linux/SELinux systems.

They simplify backup and portability.

Bind mounts are better suited for development when you want live code changes reflected instantly — but for database storage, volumes are safer and more robust.

## Testing and Validation

## Volume Mount Inspection
To confirm MongoDB volume was mounted correctly:
podman inspect <db-container-name>

Look For:
"Mounts": [
  {
    "Type": "volume",
    "Name": "mongo-data",
    "Destination": "/data/db"
  }
]

## MongoDB Task Registration
Inside the flask container:

podman exec -it <web-container-name> sh
python

Then in Python:

from pymongo import MongoClient
client = MongoClient("mongodb://db:27017/")
db = client.todo_db
list(db.todos.find())

This confirms tasks are being stored in MongoDB.

## Network Connectivity
Inside the Flask container:

podman exec -it <web-container-name> sh
python

Then:
client.server_info()

If it returns server info, MongoDB is reachable.

## Persistence of The Volume After Restart
Add a task via the app.
Run:
podman-compose down
podman-compose up

Revisit http://localhost:5000 — if the task is still there, persistence is working.

# Challenges and Resolution
Problem: Flask Container Not Starting
Cause: Missing requirements.txt or incorrect Dockerfile paths.

Fix: Move Dockerfile to root and use COPY app/requirements.txt ./ in Dockerfile.

Problem: .env Not Loaded
Cause: Podman Compose does not automatically load .env like Docker Compose.

Fix: Always run with:
podman-compose --env-file .env up --build

This explicitly loads environment variables. 
Docker Compose loads .env automatically — but Podman Compose requires manual loading.

