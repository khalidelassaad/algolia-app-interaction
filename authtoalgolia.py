import json
from algoliasearch.search_client import SearchClient

def auth():
    secrets_file = open("secrets.json", "r")
    secrets_json = json.load(secrets_file)
    secrets_file.close()
    client = SearchClient.create(secrets_json["appID"], secrets_json["writeApiKey"])
    return client