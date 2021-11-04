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

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def dfsAncestor(root, p,q):
#             # this works because first we check if this is the node that we are looking for 
            
#             if root is None: return None
#             if root.val == p.val or root.val ==q.val: return root
#             # then if not then we traverse the left then right
#             # and we buble up the node in case we find it in the lower and return that
#             # such as the same we are doing with the bubbling with the None value 
#             leftAncestor = dfsAncestor(root.left, p , q)
#             rightAncestor = dfsAncestor(root.right, p , q)
            
#             # we then return either the left or rightAncestor as a way to bubble up None and the Node 
#             if leftAncestor is None: return rightAncestor
#             # Note that the node can be the anscestor and the descendant at the same time 
#             # so if the right subtree is None then return the leftsubtree since it acted as the ancestor 
#             # and the descendant 
#             if rightAncestor is None: return leftAncestor
            
            
#             # if ever this gets hit below then we know that this node is the one that is our 
#             # ancestor since this bubbled up and the bubbled result was not None for both.
#             return root
            
            
#         return dfsAncestor(root, p, q)
    
    
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # we either find it in the left or right or this node is actually the lowest common ancestor 
        # the reason we are able to find the lowest common is because we bubble up if this is the node 
        # if ever we find none on the left and our right is one of the p or q val then we know that the lowest common will always be the right since that is one of the p and q 
        # we find this node and know that this is the lowest common ancestor that we can have because of the level and bubble it up 
        
        
        if root is None:
            return root 
        node= self.getLCA(root, p, q)
        
        return node 
    def getLCA(self, node, p, q):
        
        if node is None:
            return None 
        
        if node.val==p.val or node.val==q.val:
            return node 
        
        leftTree=self.getLCA(node.left, p,q)
        rightTree=self.getLCA(node.right, p,q)
        
        if leftTree is None:
            return rightTree
        if rightTree is None:
            return leftTree
        
        return node 

        
        

        
        
        
        
        
        
        
        
    
        
        
        
# @lc code=end

