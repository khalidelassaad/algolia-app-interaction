import json
from algoliasearch.search_client import SearchClient

def get_secrets_json():
    secrets_file = open("secrets.json", "r")
    secrets_json = json.load(secrets_file)
    secrets_file.close()
    return secrets_json

def auth():
    secrets_json = get_secrets_json()
    client = SearchClient.create(secrets_json["appID"], secrets_json["writeApiKey"])
    return client