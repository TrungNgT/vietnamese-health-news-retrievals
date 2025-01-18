from Client import client
import json

def getAllPairIndexDoc() :
    query = {
        'query': {
            'match_all': {}
        },
        'size': 10000
    }

    res = client.search(index='vinmec_with_synonyms', body=query)
    
    hits = res['hits']['hits']

    path = "../word-embedding/indexDocs.json"
    
    data = {}

    for hit in hits:
        data[hit['_id']] = hit['_source']['content']
        
    with open(file=path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

getAllPairIndexDoc()