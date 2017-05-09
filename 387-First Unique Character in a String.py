# -*- coding:utf-8 -*-
import string
class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])


'''
class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        index_list = []
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        if 1 not in dic.values():
            return -1
        for key, value in dic.items():
            if value == 1:
                index_list.append(list(s).index(key))
        return min(index_list)
'''