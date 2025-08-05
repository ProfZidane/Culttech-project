from pymongo import MongoClient
import config as cfg

config = cfg.Config()
client = MongoClient(config.MONGO_URL)

db = client[config.DATABASE_NAME]


def get_collection(collection_name):
    """
    Returns a MongoDB collection.
    
    :param collection_name: Name of the collection to retrieve.
    :return: MongoDB collection object.
    """
    return db[collection_name]



def insert_document(collection_name, document):
    """
    Inserts a document into a specified collection.
    
    :param collection_name: Name of the collection to insert into.
    :param document: Document to insert.
    :return: Inserted document ID.
    """
    collection = get_collection(collection_name)    
    result = collection.insert_one(document)
    return result.inserted_id


def insert_bulk_documents(collection_name, documents):
    """
    Inserts multiple documents into a specified collection.
    
    :param collection_name: Name of the collection to insert into.
    :param documents: List of documents to insert.
    :return: List of inserted document IDs.
    """
    collection = get_collection(collection_name)
    result = collection.insert_many(documents)
    return result.inserted_ids


def find_document_by_name(collection_name, name):
    """
    Finds a document in a specified collection by name field.
    
    :param collection_name: Name of the collection to search in.
    :param name: Name value to search for.
    :return: Found document or None if not found.
    """
    collection = get_collection(collection_name)
    return collection.find_one({"name": name})


def find_document(collection_name, query):
    """
    Finds a document in a specified collection.
    
    :param collection_name: Name of the collection to search in.
    :param query: Query to find the document.
    :return: Found document or None if not found.
    """
    collection = get_collection(collection_name)
    return collection.find_one(query)
