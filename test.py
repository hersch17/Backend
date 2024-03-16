# import requests
# import json
# import datetime
# from db_connection import db
# # res = requests.post("http://127.0.0.1:8000/tasks", data = json.dumps({"to":"me", "from":"I"}))
# # res = requests.post("http://127.0.0.1:8000/tasks", json = {"properties": {"data": datetime.datetime.now()}}  )
# # content = json.loads(res.content)
# # print(content["data"])

# db.tasks.insert_one({"date": datetime.datetime.now()})

def f(dic: dict):
    dic["heloo"] = "india"
dic = {"heloo": "world", "hi": "world"}
print(dic)
f(dic)
print(dic)