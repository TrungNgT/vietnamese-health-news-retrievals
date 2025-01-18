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
        "k": 5,
        "query_vector": q_vector
    }

    # Execute the search query
    response = client.search(index="embedded_vectors",  knn=knn_query, source=False)
    docIds = [item['_id'] for item in response['hits']['hits']]

    response = client.search(index="vinmec_with_synonyms", query={"terms":{"_id": docIds}})['hits']['hits']
    
    return response

def lexicalSearch(q: str) :
    query = {
        "query": {
        "multi_match": {
            "query": q,
            "fields": ["description", "content"]
        }
    },
    "from": 0,  
    "size": 5
    }
    response = client.search(index="vinmec_with_synonyms", body=query)['hits']['hits']
    return response

def retrieve(q: str) :

    hits = lexicalSearch(q)
    contexts = []
    
    for hit in hits :
        #contexts.append(hit['_source']['title'])
        #contexts.append(hit['_source']['description'])
        contexts.append(hit['_source']['content'])
    
    vectorSearch(q)

    return contexts
    
#retrieve("tiểu đường")


# Evaluation between LexicalSearch and VectorSearch:

def evaluation(filePath: str, resPath: str):
    with open (file=filePath, mode='r', encoding='utf-8') as file:
        quesList = file.readlines()
    
    with open (file=resPath, mode='w', encoding='utf-8') as file:
        for question in quesList:
            question = question.replace('\n', '')

            lexi_res = lexicalSearch(question)
            l_res = [item['_source']['link'] for item in lexi_res]

            vec_res = vectorSearch(question)
            v_res = [item['_source']['link'] for item in vec_res]

            str = f"QUESTION: {question}\nLRES: {'\n'.join(l_res)}\nVRES: {'\n'.join(v_res)}\n{'#' * 80}\n"
            file.write(str)

        

evaluation(filePath='../questions.txt', resPath='retrieval-evaluation.txt')