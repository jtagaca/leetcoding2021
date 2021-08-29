#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # most width
        # most height
        # second most height
        # the min of the heights multiplied by rightHeight-leftHeight+1
        # we keep going only if left and right has not moverlapped
        # check or update the max everytime

        l, r = 0, len(height)-1
        maxArea = min(height[l], height[r]) * (r-l)
        while l < r:
            tempMaxArea = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, tempMaxArea)
            # this works because we are trying to find the combination that has the
            # highest water so intially we want to find the height that has the highest value
            # in order to try and increase how much we can contain
            if height[l] < height[r]:
                l += 1
            # if the height at l then we know we can try and find a better height
            else:
                r -= 1
        return maxArea


# @lc code=end
