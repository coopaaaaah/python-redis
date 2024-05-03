import redis
import random
import json

r = redis.Redis(host='cache', port=6379, db=0)
with open("/var/data.txt", "r") as f:
    for l in f.readlines():
        r.set(l.strip(), json.dumps({ "amount": random.randint(0, 10000) }))