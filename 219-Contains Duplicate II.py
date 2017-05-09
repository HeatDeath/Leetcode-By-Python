# -*- coding:utf-8 -*-
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) <= 1:
            return False
        dic = {}
        for key, value in enumerate(nums):
            if value in dic and key - dic[value] <= k:
                return True
            dic[value] = key
        return False



'''
# --- TLE ---
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            while k >= 0:
                if i+k <= len(nums)-1:
                    if nums[i] == nums[i+k]:
                        return True
                else:
                    k -= 1
        return False
'''