# @before-stub-for-debug-begin
from python3problem136 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # guaranteed?
        # return int 
        # if we only have one element then return it 
        # stack at most half of n is still n 
        # 
        
        
        # for elements we 
        # bit XOR 
        # 2 * 2 = 0 class Solution(object):
        # bit manipulation 
        # we perform XOR 
        
        # 0
        # for value we XOR  
        #   we let bit cancel or choose
        # 1 2 3 2 1 
        # if they are different then it would add it 
        # but if it's the same then it would cancel it
        
        
        # if our value is less than the num then we add 
        # if our value is more than or equal to the num then we subtract
        value=0
        for bit in nums:
            value^=bit
        
        return value 
# @lc code=end

