# @before-stub-for-debug-begin
from python3problem101 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftRoot, rightRoot):
        if leftRoot is None or rightRoot is None:
            # this will check if both are None if they are then it will still work
            return leftRoot == rightRoot
        # we first check if our currentVal is the same then we check the left.left and right.right if both are correct then we check left.right and right.left
        # if we see something that is None then we can check if Node 3 is the same As the None
        return leftRoot.val == rightRoot.val and self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)


# @lc code=end
