from fastapi import APIRouter, Depends, HTTPException
from db_connection.mongodb import get_mongo_db
from schema.messageSchema import MessageSchema
from bson.json_util import loads, dumps
import json

from db_connection import db

# from db_connection import db

from typing import List


# @person_router.post("/api/v1/{institute}/people")
# async def add_user(user, institute: str, db=Depends(get_mongo_db) ):
#     root_collection = db.get_collection("root")
#     result = await root_collection.find_one(institute)

#     print(result)

#     if result.inserted_id:
#         return {"message": "done"}
#     else:
#         raise HTTPException(status_code=500, detail="Failed to create user")

class MessageController:
    # async def get_all_messages(db=Depends(get_mongo_db)) -> List[MessageSchema]:
    #     try:
    #         # messages_collection = db.get_collection("messages")
    #         # print(messages_collection)
    #         # result = await messages_collection.find_one()

    #         return {"message": "successs",
    #                 "data": ""}
    #     except Exception as e:
    #         print(e)
    async def get_all_messages() -> List[MessageSchema]:
        try:
            #print(db)
            mydb = db.client["basanti_backend"]
            collection = mydb["messages"]
            query = collection.find({})
            # print(query)
            return {"message": "successs",
                    "data": json.loads(dumps(query))}
            
        except Exception as e:
            print(e)
    
    async def add_message(req):
        try:
            mydb = db.client["basanti_backend"]
            collection = mydb["messages"]
            print(req)
            query = collection.insert_one(req)
            print("reached")
            return {"message": "successs",
                    }
        except Exception as e:
            print(e)

    


        
