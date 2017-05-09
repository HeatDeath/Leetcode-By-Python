# -*- coding:utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        return nums.sort(key=lambda x:1 if x==0 else 1)


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))


    # def moveZeroes(self, nums):
    #     # lastZero 用于保存 list 最前方的 0 的下标
    #     # 类比冒泡排序
    #     lastZero = 0
    #     for i in range(len(nums)):
    #         if nums[i]:
    #             nums[i], nums[lastZero] = nums[lastZero], nums[i]
    #             lastZero += 1
    #     return nums