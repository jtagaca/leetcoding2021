#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix)-1
        # O(n^2) where n is the len of height and width O(1) space
        # we go til we are not merging
        while left < right:
            # keep using to move our shifters
            # we are using right - left here because that is the way we are moving the shiters
            for i in range(right-left):
                # we update the top and bot this works because we are guaranteed to have
                # a n*n and the matrix will always be balanced in both height width
                top, bot = left, right
                # save the top left
                saveTopLeft = matrix[top][left+i]
                # we rotate the
                matrix[top][left+i] = matrix[bot-i][left]
                matrix[bot-i][left] = matrix[bot][right-i]
                matrix[bot][right-i] = matrix[top+i][right]
                matrix[top+i][right] = saveTopLeft
            left += 1
            right -= 1

# @lc code=end
