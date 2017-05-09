# -*- coding:utf-8 -*-
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums) if len(nums) != 0 else False
