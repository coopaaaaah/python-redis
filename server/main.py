import redis

r = redis.Redis(host='cache', port=6379, db=0)
v = r.get('foo')
print(v)