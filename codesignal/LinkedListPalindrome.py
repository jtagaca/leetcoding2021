# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# key trick is to find the middle then 
# reverse the right side of the slow 
# then we compare
def isListPalindrome(l):
    
    slow=fast = l 
    # find the middle using slow
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        
    
    #reverse anything from the right of slow 
    prev=None 
    while slow:
        temp=slow.next
        slow.next=prev
        prev= slow 
        slow=temp
        
        
    #compare til right is no longer valid
    left, right = l, prev
    while right: 
        if right.value != left.value:
            return False
        left=left.next
        right=right.next
    return True
         
    
    
    
    
