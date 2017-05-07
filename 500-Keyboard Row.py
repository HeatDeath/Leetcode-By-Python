# -*- coding:utf-8 -*-
import re


class Solution(object):
    def findWords(self, words):
        return list(filter(re.compile(r'^(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))


if __name__ == '__main__':
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rval = []
        dict1 = set('qwertyuiop')
        dict2 = set('asdfghjkl')
        dict3 = set('zxcvbnm')
        
        for word in words:
            tmp = set(word.lower())
            if tmp.issubset(dict1) or tmp.issubset(dict2) or tmp.issubset(dict3):
                rval.append(word)
                
        return rval

'''