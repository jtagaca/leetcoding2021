#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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
    def connect(self, root: 'Node') -> 'Node':
        # TIme and space of this ↓
        # O(n) where n is the len of the given tree
        # O(n) because we are using a que that at most will hold n values in our que
        
        
                # bfs 
        # return empty 
        # return tree 
        
        
        # empty outputs 
        # que  
        # for level in que
            # as long as the left and right are not none 
            # we pop and append childrens to que and point node.next to nextnode 
            #if lastNode in currentQue then point None  
           
            
        # return que 
        
        
        #Time and 
        # if root is None:
        #     return root 
        
        # que=[root]
        
        # while que:
            
        #     currentLenQue=len(que)
        #     currentQue=que[:]
        #     for i in range(currentLenQue):
                
        #         current=que.pop(0)
        #         if current.left is not None:
        #             que.append(current.left)
                
        #         if current.right is not None:
        #             que.append(current.right)
                    
        #         if i == currentLenQue-1:
        #             current.next=None
        #             break
        #         current.next=currentQue[i+1]
                
        # return root 
        
        
        # connecting the children 
        # while we have a current 
            # current = leftmost 
                # while we have current 
                    # we say current.left.next = current.right
                    # if current.next
                        # current.right.next= current.next.left  
                    # current = current.next 
            # leftmost=leftmost.left 
            
        #O(n) for time since we are traversing every node 
        #O(1) for space since we are not using any memory  
        if root is None:
            return root 
        
        leftmost=root
        
        while leftmost.left:
            current=leftmost
            
            while current:
                # connecting children
                current.left.next=current.right
                if current.next:
                    current.right.next=current.next.left
                    
                current=current.next
                
            leftmost=leftmost.left 
        return root 
                
# @lc code=end

