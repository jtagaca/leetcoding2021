def addTwoHugeNumbers(a, b):
    a= reverseList(a)
    b=reverseList(b)
    
    carry=0
    #our saver for the current value for next iteration
    result=None
    
    
    while a is not None or b is not None or carry>0:
        #compute value if the value is None then we need to say it is 0
        valueOfA= a.value if a is not None else 0
        valueOfB= b.value if b is not None else 0 
        value=valueOfA+valueOfB+carry
        # create a node not including carry
        node=ListNode(value%10000)
        carry=value//10000
        node.next=result
        result=node
        
        #traversing if the next node is not Null
        if a is not None:
            a=a.next
        if b is not None:
            b=b.next
            
    return result
    
def reverseList(listl):
    current=listl
    prev=None
    
    while current:
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    return prev