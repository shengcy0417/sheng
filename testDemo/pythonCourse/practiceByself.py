#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/8/1 19:32
#@Author: shengchunyue
#@File  : practiceByself.py


#登录接口，输入用户名、密码，挣钱给出提示，输错3次后锁定
_username = "shengchunyue"
_password = "1234"
count = 0
while count < 3:
    username = input("username:")
    password = input("password:")
    if username == _username and password == _password:
        print("欢迎登录！")
        break
    else:
        print("用户名或密码错误，请重试！")
        count = count + 1
        if count == 3:
            print("当前账户被锁定")


