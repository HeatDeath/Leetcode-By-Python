# -*- coding:utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)//2]


'''
class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            num_div_two = len(nums) / 2
            for num in nums[:num_div_two]:
                if nums.count(num) > num_div_two:
                    return num
'''