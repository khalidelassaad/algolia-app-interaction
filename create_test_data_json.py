import json
import random

template_record = {
    "objectID": "{}",
    "SKU": "{}",
    "name": "Product #{}",
    "image_url": "http://fakeurl.nope/{}",
    "price": "${}.{}",
    "description": "This is product #{}"
}

def generate_x_records(x):
    return_list = []
    for i in range(x):
        ith_record = template_record.copy()
        ith_record["objectID"] = ith_record["objectID"].format(i)
        ith_record["SKU"] = ith_record["SKU"].format(i)
        ith_record["name"] = ith_record["name"].format(i)
        ith_record["image_url"] = ith_record["image_url"].format(i)
        ith_record["price"] = ith_record["price"].format(random.randint(0,100), random.randint(0,99))
        ith_record["description"] = ith_record["description"].format(i)
        return_list.append(ith_record)
    return return_list

if __name__ == "__main__":
    file_to_write = open("datatoindex.ndjson", "w")
    test_data_json = generate_x_records(1000)
    for record in test_data_json:
        file_to_write.write(json.dumps(record, separators=(',', ':')) + '\n')
    file_to_write.close()