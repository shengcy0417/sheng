#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/8/1 10:10
#@Author: shengchunyue
#@File  : passwd.py


import getpass

_username = "alex"
_password = "123"

username = input("username:")
# password = getpass.getpass("password:")   #密文输入（在pycharm里面不好使，可以在命令行使用）
password = input("password:")
if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))  #format()格式化输入，括号内的数据填入{}中输出
else:
    print("invalid username")

print(username,password)