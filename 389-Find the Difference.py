# -*- coding:utf-8 -*-
class Solution(object):
    def findTheDifference(self, s, t):
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]


if __name__ == '__main__':
    # print(Solution().findTheDifference("abcd", "abcde"))
    print(Solution().findTheDifference("xfseadfasdasdasd", "xfsseadfasdasdasd"))