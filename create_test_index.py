import json
from algoliasearch.search_client import SearchClient

secrets_file = open("secrets.json", "r")
secrets_json = json.load(secrets_file)
secrets_file.close()

# Connect and authenticate with your Algolia app
client = SearchClient.create(secrets_json["appID"], secrets_json["writeApiKey"])

# Create a new index and add a record
index = client.init_index("test_index_from python")
record = {"objectID": 1, "name": "khalid is so cool"}
index.save_object(record).wait()

# Search the index and print the results
results = index.search("khalid")
print(results["hits"][0])
