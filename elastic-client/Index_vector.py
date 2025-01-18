from Client import client

client.indices.create(
    index = "embedded_vectors",
    mappings = {
        'properties': {
            'id': {
                'type': 'keyword',
            },
            'embedding_vec': {
                'type': 'dense_vector', 
            } 
        }
    }
)