import redis
from datetime import datetime

r = redis.Redis(host='cache', port=6379, db=0)

start_time = datetime.now()
counter = 0
with open("/var/data.txt", "r") as f:
    for l in f.readlines():
        r.get(l.strip())
        counter += 1

t = datetime.now() - start_time

print(f"total records: {counter}")
print(f"total read time: {t.microseconds / 1000}ms")
print(f"avg read time: {t.microseconds / 1000 / counter}ms")