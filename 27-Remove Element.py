# -*- coding:utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        nums.sort(key=lambda x: 0 if x == val else 1)
        flag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                flag = i
                break
        return len(nums[flag:])


if __name__ == '__main__':
    print(Solution().removeElement([3,2,2,3], 3))

'''
def removeElement(self, nums, val):
    try:
        while True:
            nums.remove(val)
    except:
        return len(nums)

'''