import os
import sys

elastic_client_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'elastic-client'))
sys.path.append(elastic_client_path)

word_embedding_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'word-embedding'))
sys.path.append(word_embedding_path)

from Client import client
from vectorize import embedding

#print(client.info())

def vectorSearch(q: str):
    q_vector = embedding(q).tolist()
    #print(q_vector)
    knn_query = {
        "field": "embedding_vec",
        "k": 4,
        "query_vector": q_vector
    }

    # Execute the search query
    response = client.search(index="embedded_vectors",  knn=knn_query, source=False)
    docIds = [item['_id'] for item in response['hits']['hits']]

    res_content = client.search(index="vinmec_with_synonyms", query={"terms":{"_id": docIds}})
    
    for doc in res_content['hits']['hits'] :
        print(doc['_source']['title'])

def lexicalSearch(q: str) :
    query = {
        "query": {
        "multi_match": {
            "query": q,
            "fields": ["description", "content"]
        }
    },
    "from": 0,  
    "size": 4
    }
    response = client.search(index="vinmec_with_synonyms", body=query)['hits']['hits']
    return [item['_source']['title'] for item in response]

def retrieve(q: str) :
    response = lexicalSearch(q)
    hits = response['hits']['hits']
    contexts = []
    
    for hit in hits :
        #contexts.append(hit['_source']['title'])
        #contexts.append(hit['_source']['description'])
        contexts.append(hit['_source']['content'])
    
    vectorSearch(q)

    return contexts
    
#retrieve("tiểu đường")