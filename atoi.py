class Solution:
    def myAtoi(self, s: str) -> int:
        # assume that it is positive always
        #leading zeroes are removed
        # if no number then 0
        # if the string is too large then we slice 
        # if the start is a letter then we imm return 0 
        # if the read number is not in bound of the near bound then return that near bound 
        count=0
        symbol='+'
        temp=[]
        isfloat=False
        lowbound,maxbound=-2**31, (2**31)-1
        for char in s:
            if char == " ":
                continue 
            if char=='-':
                symbol='-'
                continue
            if char.isalpha():
                break
            if char==".":
                break
            temp.append(char)
            
        if len(temp)==0:
            return 0
        
        currentNum=("").join(temp)
        
        currentNum=int(currentNum)
        if symbol=="-":
            currentNum=int(currentNum)*-1
        if currentNum<lowbound:
            currentNum=lowbound
        elif currentNum>maxbound:
            currentNum=maxbound
        return currentNum
            
        
        