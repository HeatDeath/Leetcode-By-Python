# -*- coding:utf-8 -*-
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        anagram_list = []
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                anagram_list.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return anagram_list


'''
# --- TLE ---
class Solution(object):
    def findAnagrams(self, s, p):
        p = sorted(p)
        anagram_list =[]
        for i in range(len(s)-len(p)):
            if sorted(s[i:i+len(p)]) == p:
                anagram_list.append(i)
        return anagram_list
'''