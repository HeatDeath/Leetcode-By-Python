# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0



# def maxDepth(self, root):
#     depth = 0
#     while root.left or root.right:
#         depth += 1
#         if root.left:
#             root = root.left
#         else:
#             root = root.right
#         Solution().maxDepth(root)
#     return depth