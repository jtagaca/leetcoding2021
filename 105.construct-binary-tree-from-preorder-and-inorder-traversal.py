# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # make use of the first value in the preorder 
        # find the index at value on the indorder because 
        # the values at left of index of 3 is to the right of 3 and the right are the right of 3 
        # are they unique 
        
        
        #  left and right are <= 
        # we keep going
        # if left>right return None 
        # return node 
        
        
        root = TreeNode(preorder[0])
        iDXofRoot= inorder.index(preorder[0])
        
        l,r=0,iDXofRoot-1
        root.left= self.middlePartitions(l,r,inorder)
        l,r=iDXofRoot+1,len(inorder)-1
        root.right=self.middlePartitions( l,r,inorder)
        
        return root
    
    def middlePartitions(self,l,r,inorder):
        if l>r:
            return None
        middle=(l+r)//2
        root= TreeNode(inorder[middle])
        
        root.left=self.middlePartitions( l,middle-1,inorder)
        root.right=self.middlePartitions( middle+1,r,inorder)
        
        
        return root 
# @lc code=end

