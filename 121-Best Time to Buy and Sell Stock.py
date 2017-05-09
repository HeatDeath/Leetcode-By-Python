# -*- coding:utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            # 使用 min_price 保存当前 price 之前的最小的价格
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


'''
# ---  TLE  ---
class Solution(object):
    def maxProfit(self, prices):
        current_profit = 0
        for i in range(len(prices)):
            tmp = 0
            for j in prices[i+1:]:
                tmp = j - prices[i]
                if tmp > 0:
                    current_profit = max(current_profit, tmp)
        return current_profit
'''