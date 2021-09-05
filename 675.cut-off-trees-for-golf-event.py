# @before-stub-for-debug-begin
from python3problem675 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start

import collections


class Solution:
    def cutOffTree(self, forest):
        # we found the numbers as well as the locations # finding targets
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)

        # initalize the start row and start col as well as the answer
        sr = sc = ans = 0
        for _, tr, tc in trees:
            # passing the start and the target
            d = self.bfs(forest, sr, sc, tr, tc)
            # if we found
            if d < 0:
                return -1
            ans += d
            # changing the source
            sr, sc = tr, tc
        return ans

    def bfs(self, forest, sr, sc, tr, tc):
        # initalize the end row and col
        R, C = len(forest), len(forest[0])

        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            # if we find the target then we can return the distance that we took
            # otherwise we know we did not see it and return -1
            if r == tr and c == tc:
                return d
            # if we are in bounds and we have not seen this then we can add to seen and append
            # and it exist and we can try and add to it seen or append it
            # even if it's 1 as long as we have not seen it then we can add it to the que
            # as long as we have something on the que then we can still check to see if we are able to reach
            # the target
            # but if we did not find the target and our que is 0 then we know that we did not find the target
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):

                if (
                    # as long as we are in the matrix even after checking the left and right then
                    # we can check if this position is seen or not
                    # then we check if this is 0 and if it is 0 then it is false
                    0 <= nr < R and 0 <= nc < C and
                    # what does the forest[nr, nc ] mean that as long as it is not a 0 then we
                    # append it to seen
                        (nr, nc) not in seen and forest[nr][nc] != 0):
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return -1


# @lc code=end
