# @before-stub-for-debug-begin
from python3problem236 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfsAncestor(root, p,q):
            # this works because first we check if this is the node that we are looking for 
            
            if root is None: return None
            if root.val == p.val or root.val ==q.val: return root
            # then if not then we traverse the left then right
            # and we buble up the node in case we find it in the lower and return that
            # such as the same we are doing with the bubbling with the None value 
            leftAncestor = dfsAncestor(root.left, p , q)
            rightAncestor = dfsAncestor(root.right, p , q)
            
            # we then return either the left or rightAncestor as a way to bubble up None and the Node 
            if leftAncestor is None: return rightAncestor
            # Note that the node can be the anscestor and the descendant at the same time 
            # so if the right subtree is None then return the leftsubtree since it acted as the ancestor 
            # and the descendant 
            if rightAncestor is None: return leftAncestor
            
            
            # if ever this gets hit below then we know that this node is the one that is our 
            # ancestor since this bubbled up and the bubbled result was not None for both.
            return root
            
            
        return dfsAncestor(root, p, q)
        
        
# @lc code=end

