#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

start_time = time.time()

with open('user.txt') as f_user:
    for user in f_user:
        user = user.strip('\n')
        with open('info.txt') as f:
            for line in f:
                res = line.find(user)
                if res != -1:
                    # line = line.strip('\n')
                    with open('res.txt', 'a+') as fb:
                        fb.write(line)


print('time：{}'.format(time.time()-start_time))
