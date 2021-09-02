#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    #O(n) in time and O(n) in space
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # perform dfs
        # misunderstanding
        # grow stronger to meet her one day
        # mutate given list
        # visited subArray
        # orginal
        original = image[sr][sc]
        # we thought of the base case and how can we move closer to that base case

        def dfs(image, sr, sc, newColor, original):
            if image[sr][sc] == newColor or image[sr][sc] != original:
                return
            image[sr][sc] = newColor
            if sr > 0:
                dfs(image, sr-1, sc, newColor, original)
            if sr < len(image)-1:
                dfs(image, sr+1, sc, newColor, original)
            if sc > 0:
                dfs(image, sr, sc-1, newColor, original)
            if sc < len(image[sr])-1:
                dfs(image, sr, sc+1, newColor, original)
        dfs(image, sr, sc, newColor, original)
        return image


# @lc code=end
