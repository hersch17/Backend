from fastapi import APIRouter, HTTPException, Depends, Request
from controllers.messages_controller import MessageController
from db_connection.mongodb import get_mongo_db

from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


from db_connection import db

load_dotenv()


# @asynccontextmanager
# async def lifespan(message_router: APIRouter):
#     mongo_uri = os.environ.get("MONGO_URI")
#     global client
#     global db
#     try: 
#         client = AsyncIOMotorClient(mongo_uri)
#         print("connected !")
#     except Exception as e:
#         print(e)
#     db = client.basanti_backend

#     yield
#     client.close()


message_router = APIRouter()

@message_router.get("/messages")
async def get_messages():
    return await MessageController.get_all_messages()

@message_router.post("/messages")
async def add_message(req: Request):
    req = await req.json()
    return await MessageController.add_message(req)

# @message_router.post("/messages")
# async def add_messages():
#     return MessageController.add_messages()