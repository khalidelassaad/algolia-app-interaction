# 2. Simple task - use CLI to upload "datatoindex.json" as an index)

if __name__ == "__main__":
    index_name = "khalid_test_index"
    file_to_upload_from = "datatoindex.ndjson"
    print("algolia objects import {} -F {}".format(
        index_name,
        file_to_upload_from
    ))

