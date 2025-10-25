# 🌐 Static Website with Nginx + Podman

This project demonstrates how to containerize and serve a static HTML/CSS website using **Nginx** and **Podman**. It’s designed as a beginner-friendly introduction to containerization, focusing on image creation, port mapping, and container lifecycle management — all without writing backend code.


## 📦 Project Overview

- **Goal**: Serve a static website using a containerized Nginx server.
- **Container Engine**: [Podman](https://podman.io/) — a daemonless, rootless alternative to Docker.
- **Web Server**: Nginx (Alpine-based image).
- **Content**: Simple HTML/CSS files placed in the default Nginx web root.


## 🧰 Tech Stack


**Podman** -Build and run containers
**Nginx** -Serve static content
**HTML/CSS** -Frontend content


## Commands 
podman build -t <image_name> . -Used to build the container image.
podman run -d -p 8080:80 <image_name> -Run the container image.

When you visit http://localhost:8080 in your browser, your computer sends traffic to port 8080, and Podman forwards that to port 80 inside the container — where Nginx is listening.

podman ps -List all the running containers on Podman


