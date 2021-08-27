# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        oput = []

        currentSum = 0

        for i in range(len(nums)-2):  # so that it does not go out of bounds the last one is savaing for the right pointer while the other one is for the left pointer since it is +1
            currentnumber = i
            left = currentnumber+1
            right = len(nums)-1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while left < right:
                currentSum = nums[currentnumber] + nums[left]+nums[right]
                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    oput.append([nums[currentnumber], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return oput
# @lc code=end
