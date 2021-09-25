# @before-stub-for-debug-begin
from python3problem319 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start


import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
    #     #last round always toggles the last bulb 
    #     # first we turn them on 
    #     # abstract object 
        #this works because every perfect square in the range of 
        #0-N will be the answer n=4= bulbs turned on 1 4 which are perfect squares 
        return int(math.sqrt(n))
    #     # helper function for turn off or on 
    #     # 
    #     if n==0:
    #         return 0
    #     #round 1 

    #     bulbs =["on" for x in range(n)]
    #     # every ith round after the first we turn on or off bulb
    #     #round 2
    #     for i in range(1,len(bulbs)):
    #         if i== len(bulbs)-1:
    #             self.switch(bulbs, i, False)
    #         elif (i+1)%3==0:
    #             #switch every third bulb
    #             self.switch(bulbs,i, True)
    #         else: 
    #             self.switch(bulbs,i, False)
    #     count=0
    #     for value in bulbs:
    #         if value=="on":
    #             count+=1
    #     return count
    
    # def switch(self,bulbs,i, isThird):
    #     if isThird:
    #         for i in range(1,len(bulbs)):
    #             if (i+1) % 3==0:
    #                 bulbs[i]="off" if bulbs[i]=="on" else "on"
    #     else:
    #         bulbs[i]="off" if bulbs[i]=="on" else "on"
        
                
        
        
        
# @lc code=end

