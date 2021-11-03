#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#O(logn) for time and O(d) for space where n is the given len of a tree and d is the depth of the node 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # middle or it could be itself 
        # empty input 
        # min and max of p and q 
        
        
        # is this node min<= node.val <=max
        # current max compared to node.val go left if max is < node.val
            # if node.val>max then go left 
            # else node.val< max go right 
            
        if root is None:
            return root
        
        minVal,maxVal= min(p.val,q.val), max(p.val,q.val) 
        
        node=self.getLCA(root,minVal, maxVal)
        
        return node
    
    def getLCA(self, currentNode ,minVal, maxVal):
        
        if minVal<=currentNode.val <=maxVal:
            return currentNode
        
        return self.getLCA(currentNode.left, minVal, maxVal) if currentNode.val> maxVal else self.getLCA(currentNode.right, minVal, maxVal)
            
            
            
        
            
        

        
        
        
        
        
        
        
        
        
        
# @lc code=end

