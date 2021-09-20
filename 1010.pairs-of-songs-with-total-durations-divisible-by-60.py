# @before-stub-for-debug-begin
from python3problem1010 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

import collections
# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        # this works because at each time we increment we are able to make those number of pairs 
        # key is the complement then value is the number of pairs on that complement 
        # we use the complement to see how many pairs we could make 
        result = 0
        
        for t in time:
            # 30 , 40 ,150 , 120 
            item=t%60
            complement=(60-item) %60
            if complement in remainders:
                result+=remainders[complement]
            remainders[item]+=1
            
        return result 
            
            
            
            
                
        
# @lc code=end

