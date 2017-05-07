# -*- coding:utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        nums = abs(len(bin_y) - len(bin_x))
        if len(bin_x) > len(bin_y):
            for i in range(nums):
                bin_y = '0' + bin_y

        else:
            for i in range(nums):
                bin_x = '0' + bin_x

        # print(bin_x)
        # print(bin_y)
        count = 0
        for i in range(max(len(bin_x), len(bin_y))):
            # print(i)
            # print(bin_x[-i], bin_y[-i])
            if bin_x[i] != bin_y[i]:
                count += 1
        return count


if __name__ == '__main__':
    print(Solution().hammingDistance(30, 100))