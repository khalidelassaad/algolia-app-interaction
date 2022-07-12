# 1. Set your working application with the CLI
import authtoalgolia

if __name__ == "__main__":
    secrets_json = authtoalgolia.get_secrets_json()

    print("algolia application add --name \"{}\" --app-id \"{}\" --admin-api-key \"{}\" --default".format(
        secrets_json["appName"], 
        secrets_json["appID"],
        secrets_json["writeApiKey"]
    ))

