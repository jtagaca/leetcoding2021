# @before-stub-for-debug-begin
from python3problem138 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldCopy={None:None}
        
        current=head
        
        # we're setting a map full of node as keys 
        # we then assign a none value for random pointer 
        # and the next pointer
        while current:
            copy=Node(current.val, None, None)
            #storing new nodes 
            oldCopy[current]=copy
            current=current.next
            
        current=head
        
        # this is linking it back to the old values 
        # using the current node 
        # they will be initialized to None 
        # but as we keep going we will fill them out 
        
        while current:
            copy=oldCopy[current]
            copy.next=oldCopy[current.next]
            copy.random=oldCopy[current.random]
            current=current.next
        # and this is why this works 
        return oldCopy[head]
# @lc code=end

