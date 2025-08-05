from pymongo import MongoClient
import config as cfg

config = cfg.Config()
client = MongoClient(config.MONGO_URL)

db = client[config.DATABASE_NAME]
collection_name = 'news'

def get_collection():
    return db[collection_name]



def insert_document(document):   
    collection = get_collection()    
    result = collection.insert_one(document)
    return result.inserted_id


def insert_bulk_documents(documents):  
    collection = get_collection()
    result = collection.insert_many(documents)
    return result.inserted_ids


def find_document_by_name(name):
    collection = get_collection()
    return collection.find_one({"name": name})


def find_document(query):
    collection = get_collection()
    return collection.find_one(query)
