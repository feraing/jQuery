#!/usr/bin/env python
# -*- coding:utf-8 -*-


import redis
import time

# 直连：低并发，创建连接 --- 操作 --- 释放连接

r = redis.Redis(host='127.0.0.1', port=6379, password='')
r.set('name', 'Python')
r.set('name2', 'Java')

for i in range(1, 100):
    r.set('name_%s' % i, 'Python_%s' % i)
    # time.sleep(1)


for i in range(1, 100):
    print('name_%s:' % i, r.get('name_%s' % i))



# 连接池：
# 原因：频繁直连，性能会有影响
# 条件：高并发，预先创建多个连接 --- 操作 --- 直接获取已经创建的连接操作 --- 操作完成不释放 -- 用于后续
# 获取连接的过程：
# 1. 从可用连接集合尝试获取连接；
# 2. 如果获取不到，重新创建连接；
# 3. 将获取到的连接添加到正在使用的连接集合

r_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='')
r = redis.Redis(connection_pool=r_pool)

for i in range(1, 100):
    r.set('pool_key_%s' % i, 'pool_value_%s' % i)
    # time.sleep(1)

for i in range(1, 100):
    print('pool_key_%s:%s' % (i, r.get('pool_key_%s' % i)))


# 连接池2： redis.StrictRedis
r2_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='')
r2 = redis.StrictRedis(connection_pool=r2_pool)

for i in range(1, 100):
    r2.set('r2_name_%s' % i, 'r2_value_%s' % i)
    # r2.set('r2_name_test1', 'r2_value_test1')


for i in range(1, 100):
    print('r2_name_%s:%s' % (i, r2.get('r2_name_%s' % i)))


