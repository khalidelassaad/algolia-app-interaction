# 3. More complicated task - take a snapshot of an index’s settings,
#    modify settings in the CLI, revert live version to settings from snapshot

if __name__ == "__main__":
    index_name = "khalid_test_index"
    settings_snapshot_file = "settings_snapshot.ndjson"
    
    # Save a snapshot of index's settings w/ CLI
    print("algolia settings list {} > {}".format(
        index_name,
        settings_snapshot_file
    ), end=" && ")

    # Go to dashboard and mess with settings
    # ...

    # Revert to snapshot w/ CLI
    print("algolia settings import {} -F {}".format(
        index_name,
        settings_snapshot_file
    ))
