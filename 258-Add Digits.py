# -*- coding:utf-8 -*-
class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum(list(map(int, list(str(num)))))
        return num


if __name__ == '__main__':
    print(Solution().addDigits(666))