#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers 
        # if linked list is empty 
        # returning the head 
        # O(n) O(1)
        # what happens if the n value is more than the number of values at 
        # a linked list 
        
        #two pointers 
        # dummy =head
        # l and r which will a difference of n and that is why this works
        # we want to shift our right by n 
        # then we will always have a difference of n
        # special cases are when you need to remove the first element
        # so we are using a dummy node 
        
        dummy=ListNode(-1, head)
        l,r=dummy,dummy
        copy=n
        
        while copy>0 and copy:
            r=r.next
            copy-=1
            
        while r.next is not None:
            l=l.next
            r=r.next
        #left.next should be the one getting removed
        l.next=l.next.next
        
        return dummy.next
                
# @lc code=end

