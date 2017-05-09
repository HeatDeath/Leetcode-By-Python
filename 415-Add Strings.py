# -*- coding:utf-8 -*-
class Solution(object):
    def addStrings(self, num1, num2):
        for_nums = min(len(num1), len(num2))
        carry = 0
        num3 = ''
        for i in range(1, for_nums+1):
            carry, val = divmod(int(num1[-i])+int(num2[-i])+carry, 10)
            num3 += str(val)
        if len(num1) > len(num2):
            for i in range(for_nums+1, len(num1)+1):
                carry, val = divmod(int(num1[-i]) + carry, 10)
                num3 += str(val)
        elif len(num1) < len(num2):
            for i in range(for_nums+1, len(num2)+1):
                carry, val = divmod(int(num2[-i]) + carry, 10)
                num3 += str(val)
        if carry:
            num3 += str(carry)
        return num3[::-1]


if __name__ == '__main__':
    # print(Solution().addStrings('90', '100'))
    print(Solution().addStrings('9', '99'))