# @before-stub-for-debug-begin
from python3problem74 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # is it always going to be sorted?
        # what happens empty input?
        # not sorted 
        # n* w in time and O(1) for space 
        # N*w space O(1) 
        
        # we have top right 
        # if our current ==target
            # true
        
        # if out of bounds
            # return False 
        # elif our current val > target:
            # col-=1
        # else:
            # row+=1
        
        if len(matrix)==0:
            return False
        currentR,currentC= 0, len(matrix[0])-1
        
        while currentR<len(matrix) and currentC>=0:
            current=matrix[currentR][currentC]
            if current== target:
                return True
            elif current>target:
                currentC-=1
            else:
                currentR+=1
                
        return False
# @lc code=end

