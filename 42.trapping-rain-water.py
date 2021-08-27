# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        watersOutput = 0
        # this works because we are getting the min level that we can store
        # it does not matter if we have a maxRIght of 3 if our left is smaller

        while l < r:
            # we only ever want the minimum is the key for this
            if leftMax < rightMax:
                l += 1
                # if ever our leftMax is less than our self then we update
                # and know what what we have at this cell will always be 0
                # and that is why we grab and update below
                leftMax = max(leftMax, height[l])
                watersOutput += leftMax-height[l]
            else:
                r -= 1
                # do the same thing but towards the left
                rightMax = max(rightMax, height[r])
                watersOutput += rightMax-height[r]
        return watersOutput
# @lc code=end
