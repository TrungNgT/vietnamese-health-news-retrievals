import os
import sys
import json

elastic_client_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'elastic-client'))
sys.path.append(elastic_client_path)

from Client import client

#print(client.info())

def makeQuery(q: str) :
    query = {
        "query": {
        "match": {
            "description": q
        }
    },
    "from": 0,  
    "size": 4
    }
    
    return query

def retrieve(q: str) :
    query = makeQuery(q)
    response = client.search(index="vietnamese_vinmec_doc", body=query)
    hits = response['hits']['hits']
    contexts = []
    
    for hit in hits :
        #contexts.append(hit['_source']['title'])
        #contexts.append(hit['_source']['description'])
        contexts.append(hit['_source']['content'])
    
    return contexts
    
#retrieve("tiểu đường")