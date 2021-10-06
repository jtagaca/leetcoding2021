# @before-stub-for-debug-begin
from python3problem75 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        # empty input 
        # single value 
        # return output is the same array
        
        
        # for val 
            # we check neigh to n-1 what is the lowest val of them 
            # for each val in neigh we check 
                # we are lower than our miniVal at currentIDX
                # if we do not find then we do not swap 
            # then we swap as long as our val is not the lowest 
            
            
            
        # 0, 1 1 2   
        # select the lowest value 
        # swap it with current position 
        # we go 
        
        # we are jumping too quick on coding without knowing how to actually implement it 
        # need to have a robust structure
        
        
        # selection sort also works here 
        if len(nums)==0 or len(nums)==1:
            return nums
        
        # for idx in range(len(nums)):
        #     miniVal=nums[idx]
        #     NextN=idx
        #     for nextN in range(idx+1, len(nums)):
        #         if nums[nextN]<miniVal:
        #             NextN=nextN
        #             miniVal=nums[nextN]
        #     if idx!=NextN:
        #         nums[idx], nums[NextN]= nums[NextN], nums[idx]
                
        # return nums
        # 0 1 1 1 1 1 0 2
        
        # p0 is 0 p1 is n-1 cur is 0 
        # what happens when our p2 at the end is 0 so we need the =
        
        # while cur<=p2 
            # if current is 0 then swap with p1 
                # swap p1 and cur
                # increment both 
            # if current is 2 then swap with p2 
                # swap cur with p2 
                # p2-1
            # if current is 1 then move cur by one 
    
        p1,p2,cur= 0, len(nums)-1, 0 
        # make sure that you are following the code and not the way you envisioned it 
        
        while cur<=p2:
            if nums[cur]==0:
                nums[cur], nums[p1]= nums[p1], nums[cur]
                p1+=1
                cur+=1
            elif nums[cur]==2:
                nums[cur],nums[p2]=nums[p2], nums[cur]
                p2-=1
            elif nums[cur]==1: 
                cur+=1
                
        return nums
            
            
        
# @lc code=end

