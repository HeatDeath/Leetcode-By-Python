# -*- coding:utf-8 -*-
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        for i in range(len(findNums)):
            tmp = findNums[i]
            for j in nums[nums.index(findNums[i])+1:]:
                if j > findNums[i]:
                    findNums[i] = j
                    # nums[nums.index(j)] = -1
                    break
            if findNums[i] == tmp:
                findNums[i] = -1
        return findNums


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    # print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))


