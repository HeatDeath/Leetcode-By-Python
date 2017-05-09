# -*- coding:utf-8 -*-
class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(1, len(digits)+1):
            carry, val = divmod(digits[-i] + carry, 10)
            digits[-i] = val
            if not carry:
                break
        if carry:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    print(Solution().plusOne([1, 5, 6, 7, 5]))
    print(Solution().plusOne([1, 5, 6, 7, 9]))
    print(Solution().plusOne([1, 9, 9, 9, 9]))
    print(Solution().plusOne([9, 9, 9, 9, 9]))