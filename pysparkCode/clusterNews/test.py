#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: test.py
#description: test
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-14
#log:
import collections
import re
import numpy

#def testReturn(number):
#    list_1 = []
#    list_1 = range(0,number)
#    return list_1
#
#list_2 = []
#list_2 = testReturn(10)
#print list_2


# aa = "you are right! hello world!!you are right! hello world!!you are right! hello world!!you are right! hello world!!"
# p = re.compile('''\w+''')
# bb = p.findall(aa)
# print bb
# cc = collections.Counter(bb)
# print cc

#取字典的key组织成无重复元素的序列
# aa = {"a":1, "b":2}
# bb = {"c":3, "d":4}
# cc = list(set(aa.keys()+bb.keys()))
# print cc
#字典 values函数的使用
# aa = {"a":1, "b":2, 'd':3, 'r':4, 'h':5, 'k':6}
# bb = {"a":1, "b":2, 'd':3, 'r':4, 'h':5, 'k':6}
# list_a = aa.values()
# print list_a
# list_b = bb.values()
# print list_b
# # for item in aa.keys():
# #     print aa[item]
# 二维序列的创建
# cc = [[]for i in range(0,2)]
# cc[0] = list_a
# cc[1] = list_b
# n = len(cc)
# print n
# print cc

aa = {"a":1, "b":2, 'd':3, 'r':4, 'h':5, 'k':6}
bb = {"a":1, "b":2, 'd':3, 'r':4, 'h':5, 'k':6}
cc = aa.values()
print cc
aa['r'] = 200
aa['d'] = 500
cc = aa.values()
print cc
# cc = [1,2,3,4,5,6,7]
# dd = [4,5,6,7,8,9,0]
# cc = list(set(cc+dd))
# print cc
# # cc = [{} for i in range(0,2)]
# # cc[0] = aa
# # cc[1]= bb
# # print cc
#
#
# for item in aa.items():
#     print item[1]



# aa = [1,2,3,4,5,6,7,8,9]
# bb = aa[0:2]
# print bb
