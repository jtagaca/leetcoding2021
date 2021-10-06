# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, array: List[List[int]]) -> List[int]:
        # empty input 
        # while true? 
        # 
        
        # we keep going til we overlap
        # edge case where all of us are in the same cell
        # 
        # we go right on the same row
        # we go down on the same col end 
        # go left til startcol on the endrow
        # go up til startrow+1 since we do not want to revisit the same cell
        
        sr,sc, er, ec= 0,0, len(array)-1, len(array[0])-1
        
        tempArr=[]
        while sr<=er and sc <=ec:
            for col in range(sc,ec+1):
                tempArr.append(array[sr][col])
            # this will not run since we are in the same value 1,1 
            for row in range(sr+1, er+1):
                tempArr.append(array[row][ec])
            for col in reversed(range(sc,ec)):
                # we need ↓ because we need to have a check when we have a matrix 
               
                
                # so important to have a check that the row is the same 
                # [7,9,10] if row  ↓
                # this will never run in the reversed since it will be 2,2 for column 
                if sr==er:
                    break
                tempArr.append(array[er][col])
            
            # this will not run since we are the same 1,1 for the range 
            for row in reversed(range(sr+1,er)):
                # but for th
                # +152a0jt edge case this will run since 
                 # that is [[7][9][10]] if col 
                if ec==sc:
                    break
                tempArr.append(array[row][sc])
            sr+=1
            sc+=1
            er-=1
            ec-=1
        return tempArr
            
# @lc code=end
