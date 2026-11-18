
from fastapi import FastAPI

app = FastAPI(
    title="Cloud Deployment Learning API",
    description="My first cloud deployment project",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI application!",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!"
    }
