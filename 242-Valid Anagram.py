# -*- coding:utf-8 -*-
class Solution(object):
    def isAnagram(self, s, t):
        dic1 = dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for j in t:
            dic2[j] = dic2.get(j, 0) + 1
        return dic1 == dic2



'''
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
'''