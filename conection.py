import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

def main():
    pinecone.init(api_key="4440673f-911f-4cec-b3e7-ce94157b742d", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    text = open("documentos/economia.txt", "r", encoding="utf8")
    #print(text.read())
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='arep2')
    text = open("documentos/ingenieria-civil.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='arep2')
    text = open("documentos/ingenieria-sistemas.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='arep2')
    text = open("documentos/ingenieria-electrica.txt", "r",  encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='arep2')
    text = open("documentos/ingenieria-industrial.txt", "r",  encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='arep2')

def buscar():
    pinecone.init(api_key="4440673f-911f-4cec-b3e7-ce94157b742d", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("arep2", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

if __name__ == '__main__':
    main()