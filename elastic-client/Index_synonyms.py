import os
import sys

synonyms = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vietnamese-synonyms'))
sys.path.append(synonyms)

from txt2arr_syn import txt2arr 

#txt2arr("../vietnamese-synonyms/out_n.txt")

# "Elasticsearch doesn't allow directly updating an existing mapping, so when adding synonyms or other custom analyzers, you need to create a new index with the updated settings and mappings, then reindex your data into the new index."

from Client import client

indexName = "vinmec_with_synonyms"
# cannot create existed index. 
# Please change the indexName for testing!

synlist = txt2arr("../vietnamese-synonyms/out_n.txt")
synlist.extend(txt2arr("../vietnamese-synonyms/out_v.txt"))
synlist.extend(txt2arr("../vietnamese-synonyms/out_a.txt"))

setting = {
    'number_of_shards': 1,
    'analysis': {
        'analyzer': {
            'my_vi_analyzer': {
                'type': 'custom',
                'tokenizer': 'vi_tokenizer',
                'filter': ['lowercase', 'vn_synonyms']
            }
        },
        'filter': {
            'vn_synonyms': {
                'type': 'synonym',
                'synonyms': synlist
            }

        }
    }
}

mapping = {
    'properties': {
        'content': {
            'type': 'text',
            'analyzer': 'my_vi_analyzer'
        },
        'link': {
            'type': 'text',
            'analyzer': 'standard'
        },
        'description': {
            'type': 'text',
            'analyzer': 'my_vi_analyzer'
        },
        'title': {
            'type': 'text',
            'analyzer': 'my_vi_analyzer'
        }
    }
}

client.indices.create(index=indexName, settings=setting, mappings=mapping)