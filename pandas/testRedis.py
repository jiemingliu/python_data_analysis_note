import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379);
r = redis.Redis(connection_pool=pool);
r2 = redis.Redis(connection_pool=pool);
r.set('apple','a')
print(r.get('apple'))
r2.set('banana','b')
print(r2.get('banana'))

print(r.client_list())
print(r2.client_list())