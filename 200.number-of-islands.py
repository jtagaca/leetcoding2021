# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # when to mark it properly in the visited
        # connected 1's are islands 
        # whenever we hit the traversal we know that it is 1 
        # if visited or 0 continue 
        # traverse get the top 4 store them
        # check to see if this is one and not visited, if yes then we append 
        #visited = [[]]
        seen=set()
        numIslands=0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) in seen or grid[r][c]=='0':
                    continue
                # we only traverse when it is not seen and it is not zero from here we 
                # mutate our seen and add everything that we see into the seen set 
                self.traverse(r,c, grid,seen)
                numIslands+=1
        return numIslands
    def traverse(self,r,c, grid,seen):
        
        q=[(r,c)]
        # we need to make sure we add it first in the seen before we perform the que 
        seen.add((r, c))
        while q:
            currentRow,currentCol=q.pop(0)
            # this worked and it was very simple because we were able to 
            # segment the job of every function instead of mixing them
            neighbors=self.getNeigh(currentRow,currentCol, seen, grid)
            for nr,nc in neighbors:
                    # we know that we will get neighbors that has not been visited and 
                    # not '0' so we can just append this and let the que do it's work
                    q.append((nr,nc))
        
    def getNeigh(self,currentRow,currentCol,seen, grid): 
        R,C= len(grid), len(grid[0])
        neighbors=[]
        for nr, nc in ((currentRow+1,currentCol),(currentRow-1, currentCol), (currentRow, currentCol+1), (currentRow, currentCol-1)):
            if (0<= nr < R and 0 <= nc < C and (nr,nc) not in seen and grid[nr][nc]!='0'):
                seen.add((nr,nc))
                neighbors.append((nr,nc))
                
        return neighbors 
                
        
                
                
                
    
# @lc code=end

