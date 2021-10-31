# @before-stub-for-debug-begin
from python3problem94 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left append right 
        # empty input  or root.left and root.right is none then just append value 
        # 
        
        if  root is None:
            return root
        global output 
        output=[]
        self.traverse(root)
        return output
    
    def traverse(self,root):
        if root is None:
            return
        self.traverse(root.left)
        output.append(root.val)
        self.traverse(root.right)
        
        
# @lc code=end

