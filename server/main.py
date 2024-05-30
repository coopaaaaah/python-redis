import redis
import  time
import os
from datetime import datetime, timedelta

r = redis.Redis(host='cache', port=6379, db=0)
KEY = os.getenv("KEY")

for v in range(100000):
    expiration = datetime.now() - timedelta(hours=0, minutes=1)
    end = time.mktime(expiration.timetuple())
    start = time.mktime(datetime.now().timetuple())
    v = r.zrange(KEY, int(start), int(end))
    print(f"{KEY} values in last 5 seconds: {v}")
    time.sleep(5)
