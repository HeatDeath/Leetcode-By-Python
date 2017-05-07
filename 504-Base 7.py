# -*- coding:utf-8 -*-
class Solution(object):
    def convertToBase7(self, num):
        abs_num = abs(num)
        base_str = ''
        while abs_num >= 7:
            base_str += str(int(abs_num) % 7)
            abs_num /= 7
        base_str += str(int(abs_num))
        if num >= 0:
            return base_str[::-1]
        else:
            return '-' + base_str[::-1]


if __name__ == '__main__':
    print(Solution().convertToBase7(-100))

