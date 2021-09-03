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


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # getting the requirements
        # cut off trees from low to high
        # priority que?
        # shortest to tallest
        # always unique and have no dups
        # we need to sort
        # implementation
        # how do we  know if a tree still exist?
        # duplicate?

        visited = [[False for col in forest[0]] for row in forest]
        numWalks = 0

        def gettraverse(r, c, forest, visited):

            q = [[r, c]]
            while q:
                current = q.pop(0)
                nonlocal numWalks
                numWalks += 1
                temprow, tempcol = current
                visited[temprow][tempcol] = True
                forest[temprow][tempcol] = 1
                # only grabbing neighbors that has not been visited or atleast equal to 1
                neighbors = getNeighbors(temprow, tempcol, forest, visited)

                neighbors.sort(key=lambda x: forest[x[0]][x[1]])
                for trow, tcol in neighbors:
                    neighbor = forest[trow][tcol]
                    if neighbor >= 1 and visited[trow][tcol] == False:
                        q.append([trow, tcol])

        def getNeighbors(r, c, forest, visited):
            tempList = []
            # might be a good idea to mark them visited as well
            if r > 0 and visited[r-1][c] == False:
                tempList.append([r-1, c])
            if r < len(forest)-1 and visited[r+1][c] == False:
                tempList.append([r+1, c])
            if c > 0 and visited[r][c-1] == False:
                tempList.append([r, c-1])
            if c < len(forest)-1 and visited[r][c+1] == False:
                tempList.append([r, c+1])

            return tempList
        for r in range(len(forest)):
            for c in range(len(forest)):
                # grab neighbors
                # sort neighbors
                # we append as long as the number is not Visited
                if forest[r][c] == 0:
                    return -1
                if visited[r][c]:
                    # marking only positive numbes
                    continue
                gettraverse(r, c, forest, visited)


# @lc code=end
