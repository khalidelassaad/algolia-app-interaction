import authtoalgolia

client = authtoalgolia.auth()

# Create a new index and add a record
index = client.init_index("test_index_from python")
record = {"objectID": 1, "name": "khalid is so AWESOME"}
index.save_object(record).wait()

# Search the index and print the results
results = index.search("khalid")
print(results["hits"][0])
