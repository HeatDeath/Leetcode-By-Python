# -*- coding:utf-8 -*-
class Solution(object):
    def islandPerimeter(self, grid):
        res = 0
        for i in range(len(grid)):
            # print('-----------------')
            # print('i:', i)
            for j in range(len(grid[i])):
                # print('j:', j)
                if grid[i][j]:
                    # 上
                    if i - 1 < 0:
                        res += 1
                    elif grid[i-1][j] == 0:
                        res += 1
                    # 左
                    if j - 1 < 0:
                        res += 1
                    elif grid[i][j-1] == 0:
                        res += 1
                    # 下
                    if i + 1 > len(grid)-1:
                        res += 1
                    elif grid[i+1][j] == 0:
                        res += 1
                    # 右
                    if j + 1 > len(grid[i])-1:
                        res += 1
                    elif grid[i][j+1] == 0:
                        res += 1
        return res


if __name__ == '__main__':
    print(Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))