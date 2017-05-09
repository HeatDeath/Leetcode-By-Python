# -*- coding:utf-8 -*-
class Solution(object):
    def constructRectangle(self, area):
        area_sqrt = area**0.5
        W = L = 1
        if not (area_sqrt - int(area_sqrt)):
            return (int(area_sqrt),)*2
        else:
            for i in range(1, int(area_sqrt)+1):
                value, my_mod = divmod(area, i)
                if not my_mod:
                    W, L = value, area//value
            return W, L


if __name__ == '__main__':
    print(Solution().constructRectangle(50))

