import os
from tempfile import NamedTemporaryFile
from langchain.document_loaders import PyPDFLoader


def load_pdf(pdf):
    with NamedTemporaryFile(dir='.', suffix='.pdf', delete=False) as f:
        f.write(pdf.read())
        docs =  PyPDFLoader(f.name).load()
    os.remove(f.name) 
    return docs