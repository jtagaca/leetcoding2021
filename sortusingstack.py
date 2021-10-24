# Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

# The stack supports the following operations : push, pop, peek, isEmpty.

# Input and output are both stacks

# Input : [34     ]

# Output : [3, 23, 31, 34, 92, 98]

# Input : [34, ]
# pop 31 and store in tempvar=None  
# secondstack = [3,23,31,92,98  ]

# Input : [3, 5, 1, 4, 2, 8]
# Output : [1, 2, 3, 4, 5, 8]


# sorting 
# empty input  or 1 
# are they always numbers 
# can I use the built in sort?


# stack 
# 2 stacks 

# temp=pop 
# we keep popping til temp <= to the currenttop in sec stack
    # if currentFirstTop 
    #   #save variable in temp if temp is <= currentSecondTop then keep popping the currentSecondTop
    # then append to first stack
# append 

# time will be O(n^2)where n is the len of the given stack 
# space will be O(n) 
def sortStack(stack):
    if len(stack) == 0 or len(stack) == 1:
        return stack
    
    secondStack=[]
    while stack:
        temp=stack.pop()
        currentSecondTop=secondStack[-1] if len(secondStack) >0 else None 
        
        
        while currentSecondTop is not None and temp <= currentSecondTop:
            temp2= secondStack.pop()
            stack.append(temp2)
            currentSecondTop=secondStack[-1] if len(secondStack) >0 else None 
            
        secondStack.append(temp)
            
    return secondStack
                
                
                
secondstack = [3, 23,31, 92, 98]                           
print(sortStack(secondstack))




