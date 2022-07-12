# 1. Set your working application with the CLI
import authtoalgolia

if __name__ == "__main__":
    secrets_json = authtoalgolia.get_secrets_json()

    print("algolia application add --app-id {} --admin-api-key {} -d".format(
        secrets_json["appID"], secrets_json["writeApiKey"]
    ))

