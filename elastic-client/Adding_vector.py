import json
from Client import client

with open('../word-embedding/indexEmbedded.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    client.index(index="embedded_vectors", id=item['id'], body=item)
    
print(len(data))