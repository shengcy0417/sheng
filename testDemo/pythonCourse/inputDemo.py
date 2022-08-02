#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/7/25 14:35
#@Author: shengchunyue
#@File  : inputDemo.py

#input默认输入的是字符串
username = input("username:")
password = input("password:")
print(username,password)

info = '''
----------  info of %s  ---------
name:%s
password:%s
''' %(username,username,password)

print(info)