# -*- coding:utf-8 -*-
class Solution(object):
    def findComplement(self, num):
        num = bin(num)[2:]
        # print(num)
        new_str = ''
        for i in str(num):
            if i == '1':
                i = '0'
            else:
                i = '1'
            new_str += i
        # print(new_str)
        # int_str = int(new_str, 2)
        return int(new_str, 2)

if __name__ == '__main__':
    print(Solution().findComplement(20))



'''        
class Solution(object):
    def findComplement(self, num):
        num = bin(num)[2:]
        # print(num)
        new_str = ''
        for i in str(num):
            i = int(i) ^ 1
            new_str += str(i)
        # print(new_str)
        # int_str = int(new_str, 2)
        return int(new_str, 2)
'''