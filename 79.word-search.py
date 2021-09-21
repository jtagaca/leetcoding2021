# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # if ever the len is the same as the word as well as the word is the sane then we return true 
        # traverse 
        # if the start of the word is the same then we check backtrack 
        # if o is true then we stop 
        # have a fn to get neighbors 
        
        def traverse(row,col, board, word, i, stack):
            # consider top left right bottom
            # we check if value = word[i]
            # if it is then we call traverse again newro new col i+1 
            nonlocal seen
            
            seen.add((row,col))
            if len(word)==len(stack):
                return True
            
            neighbors=getNeighbors(row,col)
            for nei in neighbors:
                tempr,tempc= nei
                if board[tempr][tempc]==word[i] and (tempr,tempc) not in seen:
                    stack.append(word[i])
                    o=traverse(tempr,tempc, board, word, i+1, stack)
                    if o == True:
                        return True
                    stack.pop()
            seen.remove((row,col))
            return False 
        def getNeighbors(row,col):
            nonlocal board, seen 
            R,C= len(board), len(board[0])
            neighbor=[]
            for nr, nc in ((row-1, col), (row+1, col), (row, col+1), (row, col-1)):
                if (0<= nr < R and 0<=nc<C and (nr, nc) not in seen):
                    neighbor.append((nr,nc))
                    
            return neighbor 
        stack=[]
        #visited 
        seen=set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    stack.append(word[0])
                    o=traverse(row,col,board, word, 1, stack)
                    if o:
                        return True
                    stack.pop()
        return False 
                    
# @lc code=end

