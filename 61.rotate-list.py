# @before-stub-for-debug-begin
from python3problem61 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k is more than the len of list 
        # return the head of the linked list 
        
        #O(n) time where n is the len of the linked list
        #O(1) space because we are not using extra memory
        # len of 1 or empty 
        # return head 
        # we get the len of the linked list 
        # len % k 
        # current pos len-k 
        # current pos
        # prev before position point to none 

            # tail.next = head
            # head = position

        if head is None or k==0:
            return head 
        
        tail=head
        lenL, tail=self.getLenLinkedList(head,tail)
        
        if lenL ==1:
            return head
        
        copy=k%lenL
        if copy!=0:
            currentIDX=lenL-copy
        else:
            return head
                
        current=head.next
        prev=dummy.next
        
        
        while current.next is not None and currentIDX>1:
            prev=prev.next
            current=current.next
            currentIDX-=1
        
        prev.next= None
        tail.next=head
        head= current
        
        return head 
    
    
    def getLenLinkedList(self, head,tail):
        current=head
        counter=0
        while current is not None:
            current=current.next
            counter+=1
            if current is not None:
                tail=current
        return [counter,tail]
    
        
# @lc code=end

