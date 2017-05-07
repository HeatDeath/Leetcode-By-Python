# -*- coding:utf-8 -*-
class Solution(object):
    def arrayPartitionI(self, my_nums):
        return sum(sorted(my_nums)[::2])