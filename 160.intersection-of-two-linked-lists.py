# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from python3problem141 import *
from typing import *
#solution ↓ O(n+m) in time since we are passing through to get the len 
# O(1) in space since we are not storing any memory
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         # empty or if len of either one is 1 then return none 
#         # cannot mutate input 
#         #getting the len of the linked list 
#         # moving forward the longer linked list by the dif of the lens 
#         # we move forward until listA.next =listB.next as long as the node.next is not null
        
#         if headA is None or headB is None:
#             return None 
#         lenA=self.getLenlink(headA)
#         lenB=self.getLenlink(headB)
        
#         if lenA==1 and lenB==1:
#             return headA
#         if lenA==1 or lenB==1:
#             return None
        
#         longer,lowest=(headA,headB) if lenA>lenB else (headB,headA)
        
#         dif= abs(lenA-lenB)
        
#         currentLongerNode= longer
#         while dif>0:
#             dif-=1
#             currentLongerNode=currentLongerNode.next
        
#         currentLowerNode=lowest
#         while currentLowerNode.next is not None:
#             if currentLowerNode.next==currentLongerNode.next:
#                 return currentLowerNode.next
#             currentLowerNode=currentLowerNode.next
#             currentLongerNode=currentLongerNode.next
            
#         return None
    
#     def getLenlink(self,LinkedList):
#         current=LinkedList
#         count=0
#         while current is not None:
#             count+=1
#             current=current.next
#         return count
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        # headA is None 
        #headB = 1 2 3 
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        
        
        
        
              
            
        
        
        
        
        
        
        
        
# @lc code=end

