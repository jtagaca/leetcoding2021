# @before-stub-for-debug-begin
from python3problem25 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we reverse 
        # we have a dummy node 
        
        # how did dummy change??
        def getKth(current,k):
            while current and k>0:
                current = current.next
                k-=1
            return current
            
        dummy=ListNode(0)
        #saves the address of 1?
        #groupprev.next will have the address of head so when we first pass we can update the value of head
        # because of the address saved and the address is unique so it will just happen on the first pass
        dummy.next=head
        groupPrev=dummy
        # we change the head address?
        while True:
            kth=getKth(groupPrev,k)
            if kth is None:
                break
            groupnext=kth.next
            prev, current=groupnext, groupPrev.next
            while current != groupnext:
                temp=current.next
                current.next=prev
                prev=current
                current=temp
            
            
            # logic error?
            # we changed dummy here??
            # after the first iteration
            tmp=groupPrev.next
            # saving the value 
            #address of dummy.next which has the address of head was updated on the first iteration
            #repointing dummy.next to the kth 
            groupPrev.next=kth
            #severing the link from dummy to 1
            groupPrev=tmp
            #how are we returning dummy.next here?
            #isn't dummy.next ==head? and head is still pointing to original
        return dummy.next
            
            
            
            
            
        
        #get the kth element 
        
        
        
        
# @lc code=end

