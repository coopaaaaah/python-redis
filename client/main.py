import redis

r = redis.Redis(host='cache', port=6379, db=0)
r.set('foo', 'bar')