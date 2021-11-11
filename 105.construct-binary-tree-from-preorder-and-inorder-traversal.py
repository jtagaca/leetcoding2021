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
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # make use of the first value in the preorder 
#         # find the index at value on the indorder because 
#         # the values at left of index of 3 is to the right of 3 and the right are the right of 3 
#         # are they unique 
        
        
#         #  left and right are <= 
#         # we keep going
#         # if left>right return None 
#         # return node 
        
        
#         root = TreeNode(preorder[0])
#         iDXofRoot= inorder.index(preorder[0])
        
#         l,r=0,iDXofRoot-1
#         root.left= self.middlePartitions(l,r,inorder)
#         l,r=iDXofRoot+1,len(inorder)-1
#         root.right=self.middlePartitions( l,r,inorder)
        
#         return root
    
#     def middlePartitions(self,l,r,inorder):
#         if l>r:
#             return None
#         middle=(l+r)//2
#         root= TreeNode(inorder[middle])
        
#         root.left=self.middlePartitions( l,middle-1,inorder)
#         root.right=self.middlePartitions( middle+1,r,inorder)
        
        
#         return root 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


preorderIDX =0


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # create a hashmap from inordertraversal to use as indeces for building left and right sub trees 
        # pre order index to create nodes from this 
        
        # construct left from left, map[root_value]-1
        # build right from map[root_val]+1
        
        # ret root
        
        
        
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        hashm={}
        
        for idx, val in enumerate(inorder):
            hashm[val]=idx
        
        
        
        
        return self.buildnodetree(0, len(inorder)-1, preorder, hashm)
            
    def buildnodetree(self, left, right , preorder, hashm):
        global preorderIDX
        if left>right:
            return None
        
        
        root=TreeNode(preorder[preorderIDX])
        preorderIDX+=1
        
        root.left=self.buildnodetree(left, hashm[root.val]-1, preorder, hashm)
        root.right=self.buildnodetree(hashm[root.val]+1, right, preorder, hashm)
        
        return root 

        
        
        
        
    
        
        
        
        
        
# @lc code=end

