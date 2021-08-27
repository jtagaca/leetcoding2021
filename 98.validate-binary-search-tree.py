# @before-stub-for-debug-begin
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValidTree(root, float("-inf"), float("inf"))


def isValidTree(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.val < minValue or tree.val >= maxValue:
        return False
    leftisValid = isValidTree(tree.left, minValue, tree.val)
    rightisValid = isValidTree(tree.right, tree.val, maxValue)

    return leftisValid and rightisValid

# @lc code=end
