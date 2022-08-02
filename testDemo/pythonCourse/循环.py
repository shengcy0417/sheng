#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/8/1 10:49
#@Author: shengchunyue
#@File  : 循环.py

# count = 0
# while True:
#     print("count:",count)
#     count = count + 1
#     if count == 1000:
#         break

# for i in range(0,10):
#     if i<3:
#         print("loop",i)
#     else:
#         continue #跳出本次循环，进入下一个循环
#         # break #结束本次循环
#     print("haha")


for i in range(10):
    print("----------",i)
    for j in range(10):
        print(j)
        if j>5:
            break