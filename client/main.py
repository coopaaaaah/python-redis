import redis
import random
import json
from datetime import datetime
from enum import Enum

class Type(Enum):
    TRANSACTION = "TRANSACTION"
    ACTION = "ACTION"

r = redis.Redis(host='cache', port=6379, db=0)
start_time = datetime.now()
counter = 0
with open("/var/data.txt", "r") as f:
    for l in f.readlines():
        r.set(l.strip(), json.dumps({ "amount": random.randint(0, 10000),"type": random.choice(list(Type)).value }))
        counter += 1
t = datetime.now() - start_time

print(f"total records: {counter}")
print(f"total write time: {t.microseconds / 1000}ms")
print(f"avg write time: {t.microseconds / 1000 / counter}ms")