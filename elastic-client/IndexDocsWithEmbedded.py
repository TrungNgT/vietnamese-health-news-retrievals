import os
import sys

embedding_vector = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'word-embedding'))
sys.path.append(embedding_vector)

from vectorize import embedding

from Client import client
from elasticsearch import helpers
import json

#indexName = "vietnamese_vinmec_doc"
indexName = "vinmec_syno_embedded1"

#jsonFile_list = ['news301_400.json', 'news401_500.json', 'news501_600.json', 'news601_700.json', 'news701_800.json']
# adding new here.
jsonFile_list = ['news1_100.json', 'news101_200.json', 'news201_300.json', 'news301_400.json', 'news401_500.json', 'news501_600.json', 'news601_700.json', 'news701_800.json']

actions = []

for file_name in jsonFile_list :
    path = '../news/' + file_name
    #print(path)
    with open(path, "r", encoding='utf-8') as file :
        raw_data = json.load(file)

    actions.clear()

    for item in raw_data:
        passage = item['content']
        item['embedded_vector'] = embedding(passage)
        print(item['embedded_vector'])
        #client.index(index=indexName, document=item)
        action = {"_op_type": "index", "_index": indexName, "_source": item}
        actions.append(action)

    success, failed = helpers.bulk(client, actions)
    print(f"Successfully indexed {success} documents.")
    print(f"Failed to index {failed} documents.")