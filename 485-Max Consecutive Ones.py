# -*- coding:utf-8 -*-
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        tmp, result = 0, 0
        for num in nums:
            if num:
                tmp += 1
                result = max(tmp, result)
            else:
                tmp = 0
        return result


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]))


'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count_list = []
        for i in range(len(nums)):
            count = 0
            if nums[i]:
                for j in nums[i:]:
                    if j:
                        count += 1
                    else:
                        break
                count_list.append(count)
        if len(count_list) > 0:
            return max(count_list)
        else:
            return 0
'''
