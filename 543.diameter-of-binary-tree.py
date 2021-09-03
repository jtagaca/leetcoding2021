# @before-stub-for-debug-begin
from python3problem543 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get the max of the left or right +1
        # if node is none stop
        diameter = 0

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left+right)
            return max(left, right) + 1
        dfs(root)
        return diameter
# @lc code=end
