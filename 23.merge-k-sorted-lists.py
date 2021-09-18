# @before-stub-for-debug-begin
from python3problem23 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

from queue import PriorityQueue


#have a space of O(n*m log(n*m)) where n is the len of a linked list 
# and m is the len of the max num of a linked list 
# space will be O(n*m) because we will be storing at most that values


class Solution():
    def mergeKLists(self, lists):
        dummy=head = ListNode(0)
        q = PriorityQueue()
        # priority queue will always be sorted when using q.get()
        # for every list 
        for l in lists:
            current=l
            while current:
                #q.put() means it's adding to the q 
        # we append every node 
                q.put(current.val)
                current=current.next
                
        # since we have a sorted values we can just 
        # create the node and repoint head
        while not q.empty():
            #head.next was updated here 
            head.next=ListNode(q.get())
            head=head.next
            
            
        return dummy.next
    
    
    
# @lc code=end

