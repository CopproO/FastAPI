from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Endpoint to write data to the database
@app.post("/data")
def write_data(data: dict):
    collection.insert_one(data)
    return {"message": "Data added successfully"}

# Endpoint to provide real-time updates
@app.websocket("/updates")
async def updates_websocket(websocket: WebSocket):
    await websocket.accept()
    async for _ in collection.watch():
        data = collection.find_one()
        await websocket.send_json(data)
