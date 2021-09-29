#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # input string
        # string
        # empty input 
        # carry over 
        # if it's 2 then we carry over 
        # start from the end 
        # 
        
        # we keep going til we have something or we have a carry
        # start from the end 
        # if b is in bounds then int b
        # if a is in bounds then int a
        # if added value +carry % 2 ==0
        #   carry +=1
        # append new value to an array at the start
        # join string
        # return string
        #O max(n,m) because we are choosing either max of len of n or m
        if (int(a[0])==0 and int(b[0])==0):
            return "0"
        
        carry=0
        aIDX,bIDX=len(a)-1, len(b)-1
        tempArr=[]
        while aIDX >=0 or bIDX >= 0 or carry>0:
            valueA= int(a[aIDX])if aIDX>=0 else 0
            valueB= int(b[bIDX]) if bIDX>=0 else 0
            
            totalValue=valueA+valueB
            
                
            if carry>0:
                totalValue+=carry
                carry-=1
            if totalValue>1:
                totalValue=totalValue-2
                carry+=1
                
            tempArr.insert(0, str(totalValue))
            aIDX-=1
            bIDX-=1
            
        outputString=("").join(tempArr)
        return outputString
                
            
            
            
            
            
        
         
# @lc code=end

