from Client import client
import json

#indexName = "vietnamese_vinmec_doc"
indexName = "try_999_with_noun_syn"

#jsonFile_list = ['news301_400.json', 'news401_500.json', 'news501_600.json', 'news601_700.json', 'news701_800.json']
# adding new here.
jsonFile_list = ['news1_100.json']

for file_name in jsonFile_list :
    path = '../news/' + file_name
    #print(path)
    with open(path, "r", encoding='utf-8') as file :
        data = json.load(file)
    
    for item in data:
        client.index(index=indexName, document=item)
    
    print(len(data))