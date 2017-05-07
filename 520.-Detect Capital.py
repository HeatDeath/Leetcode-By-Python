# -*- coding:utf-8 -*-
import re


class Solution(object):
    def detectCapitalUse(self, word):
        pattern = re.compile(r'[A-Z]{1}')
        return_list = pattern.findall(word)
        # print(return_list)
        if len(return_list) == len(word):
            return True
        elif len(return_list) == 1 and return_list[0] == word[0]:
            return True
        elif len(return_list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().detectCapitalUse('USA'))
    print(Solution().detectCapitalUse('uSA'))
    print(Solution().detectCapitalUse('usa'))