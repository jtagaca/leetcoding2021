# @before-stub-for-debug-begin
from python3problem33 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
# time will be O(logn) because we are having the array each time 
# the space will be O(1) since we are not using extra memory 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min l # max r 
        #check which is the sorted partition
        #binary search 
        #target is in range of the current partition
        l,r= 0, len(nums)-1
        #[4,5,6,7,0,1,2]
        #0
        #0+6
        #6//2 =3 
        #middle=7
        # this works because we are either selecting 
        # the correct partitioned array for each time 
        # and so we then check if the value is within our range 
        # if it does then it we will just update our middle
        while l<=r:
            middle=(l+r)//2
            
            currentMiddle=nums[middle]
            if currentMiddle==target:
                return middle
               #check which is the sorted partition
            if nums[l]<currentMiddle:
                #left sorted partition
                if target>=nums[l] and target<currentMiddle:
                    r= middle-1
                else:
                    l= middle+1
                    
            else:
                if target==nums[r]:
                    l=middle+1
                if target<=nums[r] and target>currentMiddle:
                    l=middle+1
                else:
                    r=middle-1
        return -1
        
# @lc code=end

