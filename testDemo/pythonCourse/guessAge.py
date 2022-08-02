#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/8/1 10:25
#@Author: shengchunyue
#@File  : guessAge.py


count = 0
age_of_oldboy = 56
# while True:
#     if count == 3:
#         break
while count < 3:
# for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it!")
        if guess_age == age_of_oldboy:
            break
    elif guess_age > age_of_oldboy:
        print("think smaller^")
    else:
        print("think bigger^")
    count += 1
    print(count)
    if count == 3:
        countinue_confirm = input("Do you want tu keep guessng..?")
        if countinue_confirm != 'n':
            count = 0

# print("you have tried too many times....")


# for i in range(0,10,2):
#     print("loop",i)