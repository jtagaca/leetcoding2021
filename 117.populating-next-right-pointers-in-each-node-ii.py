#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connectingNodes(self, currentChild, prev, leftmostNode):
        if currentChild is None:
            return prev, leftmostNode
        
        if prev: 
            prev.next= currentChild
            
        else:
            leftmostNode=currentChild 
            
        prev=currentChild
        
        return prev, leftmostNode
        

    
    def connect(self, root: 'Node') -> 'Node':
        
        
        # repointing children and finding the most leftnode 
        # empty input 
        
        # we start with root as the leftnode
        # prev, current = none, leftmost 
        # leftmost =None 
           
            # while current 
                # we pass in childrens as a ways to check and create a flag for leftmost
                # finding the leftmost or prev repointing to childnode 
                # every time we need to update prev to update to child
                # returning prev,leftmost 
                
                # current = current.next 
        
            
        # if ever we do not update leftmost then we know we are done 
        
       
        leftmostNode= root 
        while leftmostNode:
            nextLevelprevVal, currentLevelNode=None, leftmostNode
            
            leftmostNode=None 
            
            while currentLevelNode:
                
                nextLevelprevVal, leftmostNode= self.connectingNodes(currentLevelNode.left, nextLevelprevVal, leftmostNode)
                nextLevelprevVal, leftmostNode=self.connectingNodes(currentLevelNode.right, nextLevelprevVal, leftmostNode)
                
                currentLevelNode= currentLevelNode.next
                
        return root 
                
            
            


# @lc code=end

