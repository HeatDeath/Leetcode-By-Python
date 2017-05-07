# -*- coding:utf-8 -*-
class Solution(object):
    def twoSum(self, numbers, target):
        # 以 k 为指针
        k = 0
        # 遍历 nums list
        for i in numbers:
            # j 为另一个数
            j = target - i
            # 指针后移
            k += 1
            # rest_nums 为 nums 的剩余部分
            rest_nums = numbers[k:]
            # 如果 j 在 rest_nums 中
            if j in rest_nums:
                # 则返回 i 和 j 的下标
                return [k, rest_nums.index(j) + k+1]


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 17))