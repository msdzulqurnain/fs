import pymongo, os
from config import MONGO_URI, DB_NAME


dbclient = pymongo.MongoClient(MONGO_URI)
database = dbclient[DB_NAME]

user_data = database['users']

async def cek(user_id : int):
    ada = user_data.find_one({'id': user_id})
    return bool(ada)

async def tambah(user_id: int):
    user_data.insert_one({'id': user_id})
    return

async def semua():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['id'])
        
    return user_ids

async def hapus(user_id: int):
    user_data.delete_one({'id': user_id})
    return
