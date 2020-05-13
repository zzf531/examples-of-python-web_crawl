import pymongo
import json
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.gs
collection = db.gs500
results = collection.find_one({}, {'_id': False})
results2 = collection.find({}, {'_id': False})
db.collection.find({}, {'_id': False})

print(results2)
for result in results2:
    # json_string = json.dumps(result)
    # print(json_string)
    with open('data500.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(result, ensure_ascii=False) + '\n')
