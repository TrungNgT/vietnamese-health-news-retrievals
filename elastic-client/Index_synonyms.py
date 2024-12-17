from Client import client

indexName = "vietnamese_vinmec_doc"
# cannot create existed index. 
# Please change the indexName for testing!

setting = {
    'number_of_shards': 1,
    'analysis': {
        'analyzer': {
            'my_vi_analyzer': {
                'type': 'custom',
                'tokenizer': 'vi_tokenizer',
                'filter': 'lowercase'
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