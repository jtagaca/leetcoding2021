# @before-stub-for-debug-begin
from python3problem124 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # perform traversal
        # we split
        # we buble onesided left right max because is only one sided
        MaxPath = [root.val]

        def dfs(root):
            if root is None:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # performing a check to see if it is negative because we will have
            # to add and compute what is the maximum output per node
            # if negative then we can choose to ignore it
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            # adding the current sum
            currentVal = leftMax + rightMax + root.val
            MaxPath[0] = max(MaxPath[0], currentVal)
            # choose which side to return if there are more than one split
            return root.val + max(leftMax, rightMax)
        dfs(root)

        return MaxPath[0]
# @lc code=end
