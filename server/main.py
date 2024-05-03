import redis
import json

r = redis.Redis(host='cache', port=6379, db=0)

with open("/var/data.txt", "r") as f:
    for l in f.readlines():
        print(json.loads(r.get(l.strip())))