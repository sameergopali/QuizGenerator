#Function to push data to Vector Store - Pinecone here
import pinecone
from pinecone import NotFoundException, ApiException
from langchain.vectorstores import Pinecone

def push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,docs):
    pinecone.init(
        api_key=pinecone_apikey,
        environment=pinecone_environment
        )
    if index_exists(pinecone_index_name):
        delete_index(pinecone_index_name)
    create_index(pinecone_index_name)
    index = Pinecone.from_documents(docs, embeddings, index_name=pinecone_index_name)
    return index
 


#Function to pull infrmation from Vector Store - Pinecone here
def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):

    pinecone.init(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name

    index = Pinecone.from_existing_index(index_name, embeddings)
    return index


def index_exists(index_name):
    indexes = pinecone.list_indexes()
    return index_name in indexes


def delete_index(index_name):
    try:
        pinecone.delete_index(name=index_name)
    except NotFoundException:
        print("error deleting")


def create_index(index_name):
    try:
        pinecone.create_index(name=index_name, dimension=384)
    except ApiException:
        print("ApiException")
