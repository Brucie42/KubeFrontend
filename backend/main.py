from fastapi import FastAPI
import os
import socket

app = FastAPI()

@app.get("/api")
def home():
    pod_name = os.getenv("HOSTNAME", "unknown")
    return {
        "message": "Hello from Kubernetes!",
        "pod": pod_name,
        "host": socket.gethostname()
    }

@app.get("/api/reverse/{text}")
def reverse_text(text: str):
    return {"original": text, "reversed": text[::-1]}
