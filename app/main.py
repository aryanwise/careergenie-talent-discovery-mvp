# For later use when connecting to backend

from fastapi import FastAPI
from app.github import search_users

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CareerGenie MVP API running"}


@app.get("/search")
def search(query: str):
    users = search_users(query)
    return users