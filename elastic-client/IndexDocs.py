from Client import client
from CreateIndex import indexName
import json

jsonFile_list = ['news1_100.json']
# adding new here.

for file_name in jsonFile_list :
    path = '../news/' + file_name
    #print(path)
    with open(path, "r", encoding='utf-8') as file :
        data = json.load(file)
    
    for item in data:
        client.index(index=indexName, document=item)
    
    #print(len(data))