# @before-stub-for-debug-begin
from python3problem403 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#


#time is 3^n and space is 3^n because we are storing and considering at most 3 per element
# @lc code=start
class Solution(object):
    def canCross(self, stones):
        # have a positions that are available 
        # removal of duplicate paths
        # we have a prevJump of the prev
        # we could do this 3n 
        # because for each time we consider 3 nodes
        seen=set()
        stoneSet=set(stones)
        stack=[(0,0)]
        end=stones[-1]
        
        while stack:
            currentVal, prevJump= stack.pop()
            if (currentVal,prevJump) in seen:
                continue
            seen.add((currentVal,prevJump))
            # consider the 3 positions 
            if currentVal==end:
                return True
            for jump in range(prevJump-1, prevJump+2):
                if jump<=0:
                    continue
                if currentVal+jump in stoneSet:
                    stack.append((currentVal+jump, jump))
        return False
            
            
            
        
        
        
        
        
        
        
        
        
        # @lc code=end

