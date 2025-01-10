import os
import sys

embedding_vector = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'word-embedding'))
sys.path.append(embedding_vector)

from vectorize import embedding

import json
path = "../news/news1_100.json"

data = []

with open(path, "r", encoding='utf-8') as file :
    raw_data = json.load(file)
    
    data.clear()

    for item in raw_data:
        passage = item['content']
        item['embedded_vector'] = embedding(passage)
        data.append(item)
        #client.index(index=indexName, document=item)

    # Remove the incorrect line
    # json_lines = raw_data.strip().splitlines()

    # Reformat each JSON object into a single-line dictionary
