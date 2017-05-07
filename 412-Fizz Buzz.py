# -*- coding:utf-8 -*-
class Solution(object):
    def fizzBuzz(self, n):
        new_list = []
        for i in range(1, n+1):
            if i % 15 == 0:
                new_list.append('FizzBuzz')
            elif i % 5 == 0:
                new_list.append('Buzz')
            elif i % 3 == 0:
                new_list.append('Fizz')
            else:
                new_list.append(str(i))
        return new_list


if __name__ == '__main__':
    print(Solution().fizzBuzz(10))