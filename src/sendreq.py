import requests
from pymongo import MongoClient

client = MongoClient()
db = client['benchmark']
new_product_collection = db['res_time']


def test_req_perf(api_url, target_url, target_method, key, conc):
    res = requests.post(api_url, json={"key": key, "url": target_url, "method": target_method})
    if res.status_code != 200:
        return None
    
    new_product_collection.insert_one({"concurrency": conc, "res_time": res.elapsed.total_seconds()})
    return res.content.decode()
    
