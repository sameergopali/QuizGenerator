
from modules.pinecone_utils import push_to_pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


#Create embeddings instance
def create_embeddings():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings


def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=chunk_overlap, chunk_size=chunk_size)
    docs =  text_splitter.split_documents(documents)
    return docs


def index_pdf(pdf_doc):
    docs = split_docs(pdf_doc)
    embeddings =  create_embeddings()
    index =  push_to_pinecone(os.environ.get("PINECONE_API_KEY"),"gcp-starter","mcq" ,embeddings,docs)
    return index