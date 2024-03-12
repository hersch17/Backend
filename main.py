from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
from routers.messageRouter import message_router
from db_connection.mongodb import get_mongo_db
import asyncio


from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

#pymongo
from db_connection import db
import uvicorn

load_dotenv()
@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_uri = os.environ.get("MONGO_URI")
    db.connect_to_database(path=mongo_uri)
    print("connected to db in main.py!")

    yield
    db.client.close()
    # client.close()

app = FastAPI(lifespan= lifespan)



#changes 
# from motor.motor_asyncio import AsyncIOMotorClient
# import os
# mongo_uri = os.environ.get("MONGO_URI")
# client = AsyncIOMotorClient(mongo_uri)
# db = client["basanti_backend"]
# async def get_database():
#     try:
#         yield db
#     finally:
#         client.close()
# #changes




# @app.post("/api/v1/initialise/{institute}")
# async def initialise_root(institute: str, db=Depends(get_mongo_db)):
#     root_data = {"Name" : institute, "People": {}, "Events": {}, "Inventory": {}}
#     root_collection = db.get_collection("root")
#     result = await root_collection.insert_one(root_data)

#     if result.inserted_id:
#         return {"message": "User created successfully", "user_id": str(result.inserted_id)}
#     else:
#         raise HTTPException(status_code=500, detail="Failed to create user")
app.include_router(message_router)


