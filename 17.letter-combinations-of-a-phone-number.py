# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # map of the coresponding letters 
        # hard to do for loop 
        # recursion 
        # 
        # if curString == len(digits):
            # viable string 
        # iterate over a map for value 
        # 
        result=[]
        characters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(i, currentString):
            if len(currentString)==len(digits):
                tempStr=("").join(currentString)
                result.append(tempStr)
                return 
            for c in characters[digits[i]]:
                currentString.append(c)
                # back track means you add then you remove after using it 
                # we added and tested
                # you use it and explore if it is viable 
                # if ever it hits your base case then great if not then ok
                backtrack(i+1, currentString)
                # then we popped what we used or removed it 
                currentString.pop()
        
        tempArr=list()
        if digits:
            backtrack(0,tempArr)
        
        
        return result 
# @lc code=end

