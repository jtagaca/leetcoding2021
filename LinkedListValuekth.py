# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    #removing the value k in l 
    # return the linked list 
    #special cases when it is the head 
    # if our next is k then we just say current.next = current.next.next 
    
    # this works because we are just 
    # finding the values and once we find the values that has that we 
    # know that our prev value is the one that needs to be repointed 
    # if the value is our head then we can just chop it off using our return statement
    current=l
    # removed our value from 1-> len of LinkedList
    while current:
        if current.next and current.next.value==k:
            current.next=current.next.next
        else:
            current=current.next
    return l.next if l and l.value ==k else l     
        
    
    

