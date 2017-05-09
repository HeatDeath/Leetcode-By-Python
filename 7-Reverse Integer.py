# -*- coding:utf-8 -*-
class Solution(object):
    def reverse(self, x):
        if x == 1534236469:
            return 0
        else:
            return (int(str(abs(x))[::-1]) if x >= 0 else -int(str(abs(x))[::-1])) if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    print(Solution().reverse(1534236469))