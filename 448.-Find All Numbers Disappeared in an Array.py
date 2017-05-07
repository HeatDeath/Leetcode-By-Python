# -*- coding:utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

'''
# 理解错了题意
class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums = list(set(sorted(nums)))
        # print(nums)
        lost_list = []
        for i in range(len(nums)):
            if i+1 == len(nums):
                break
            elif nums[i+1] - nums[i] != 1:
                tmp = nums[i]
                while tmp < nums[i+1]-1:
                    tmp += 1
                    lost_list.append(tmp)
        return lost_list
'''

'''
# TLE
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        nums = list(set(nums))
        lost_list =[]
        for i in range(1, n+1):
            if i in nums:
                pass
            else:
                lost_list.append(i)
        return lost_list
'''