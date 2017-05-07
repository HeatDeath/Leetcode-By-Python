# -*- coding:utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        str_list = s.split(' ')
        for i in range(len(str_list)):
            str_list[i] = str_list[i][::-1]
        s = ' '.join(i for i in str_list)
        return s


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
