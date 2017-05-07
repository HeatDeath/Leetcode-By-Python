# -*- coding:utf-8 -*-
class Solution(object):
    def matrixReshape(self, nums, r, c):
        sum_length = 0
        for i in range(len(nums)):
            sum_length += len(nums[i])
        if sum_length != r*c:
            return nums
        else:
            true_nums = []
            for i in range(len(nums)):
                true_nums += nums[i]
            # print(true_nums)
            new_nums = []
            for i in range(r):
                new_nums.append(true_nums[c*i:c*(i+1)])
                # print(new_nums[i])
            return new_nums


if __name__ == '__main__':
    print(Solution().matrixReshape([[1], [2], [3], [4]], 2, 2))

