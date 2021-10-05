# @before-stub-for-debug-begin
from python3problem141 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # return true or false
        # empty input
        # can a single node be a cyvle?
        
        # two pointers
        # move fast by 2 
        # start the slow and fast 
        # if two pointers are at the same node 
        #   then return true
        # but if our fast pointer reaches the end 
            # turn false
        
        if head is None:
            return False
        
        slow, fast = head,head
        counter=2
        while counter>0 and fast is not None:
            fast=fast.next
            counter-=1
        while fast is not None:
            if slow ==fast:
                return True
            slow=slow.next
            fast= fast.next
        return False
            
# @lc code=end

