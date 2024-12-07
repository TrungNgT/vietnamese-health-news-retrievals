from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "FokPpOKqXaEC+ItgCdKQ"

client = Elasticsearch(
    hosts="http://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD)
    # insert ca_cert if you serve the elasticsearch cluster with https:// on your local machine.
)

#print(client.info())