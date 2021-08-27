# @before-stub-for-debug-begin
from python3problem103 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Que = [root]
        level = 1
        result = []
        if root is None:
            return
        while Que:
            temp = []
            lenQue = len(Que)
            # a way to keep track of the level and how many nodes are
            # in that level
            for i in range(lenQue):
                current = Que.pop(0)
                if current is None:
                    continue
                temp.append(current.val)
                if current.left != None:
                    Que.append(current.left)
                if current.right != None:
                    Que.append(current.right)
            # if we have a even level then we flip the list from right to left
            if level % 2 == 0:
                result.append(temp[::-1])
            # otherwise we use left to right
            else:
                result.append(temp[::])
            level += 1
        return result


# @lc code=end
