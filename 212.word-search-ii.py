# @before-stub-for-debug-begin
from python3problem212 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # if ever the len is the same as the word as well as the word is the sane then we return true 
        # traverse 
        # if the start of the word is the same then we check backtrack 
        # if o is true then we stop 
        # have a fn to get neighbors 
        
        
        # return the word 
        def traverse(row,col, board, word, i, stack):
            # consider top left right bottom
            # we check if value = word[i]
            # if it is then we call traverse again newro new col i+1 
            nonlocal seen
            
            seen.add((row,col))
            if len(word)==len(stack):
                tempStr=("").join(stack)
                return tempStr
            
            neighbors=getNeighbors(row,col)
            for nei in neighbors:
                tempr,tempc= nei
                if board[tempr][tempc]==word[i] and (tempr,tempc) not in seen:
                    stack.append(word[i])
                    o=traverse(tempr,tempc, board, word, i+1, stack)
                    if o != "":
                        return o
                    stack.pop()
            seen.remove((row,col))
            return "" 
        
        
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
        prev=0
        result =[]
        for word in words:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]==word[0]:
                        stack.append(word[0])
                        o=traverse(row,col,board, word, 1, stack)
                        if o != "":
                            result.append(o)
                            stack=[]
                            break
                        stack=[]
                # if we have added a new result 
                # then we know that we do not need to check the same word again
                # 
                if len(result)> prev:
                    prev+=1
                    break
            seen=set()

        return result  


# @lc code=end

