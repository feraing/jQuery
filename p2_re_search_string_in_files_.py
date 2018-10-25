#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import time

start_time = time.time()

# user = '变速器'
# with open('user.txt') as f_user:
#     for u in f_user:
#         res = re.search(user, u)
#         if res:
#             print(u)

        # res = re.match(user, u)
        # match:从开头进行匹配
        # if res:
        #     print(res.group())

with open('user.txt') as f_user:
    for user in f_user:
        user = user.strip('\n')
        with open('info.txt') as f_infos:
            for info in f_infos:
                res = re.search(user, info)
                if res:
                    # print(info)
                    with open('res.txt', 'a+') as f_res:
                        f_res.write(info)


print('time：{}'.format(time.time()-start_time))
# time：0.0429999828339
