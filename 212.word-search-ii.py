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


class TrieNode: 
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        current=self
        for c in word:
            if c not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        cur.isWord=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #adding nodes 
        root=TrieNode()
        # creating the trienode 
        for w in words:
            root.addWord(w)
            
        R, C = len(board), len(board[0])
        res, visit= set(), set()
        
        def dfs(r, c node, word):
            if (r <0 or c< 0  or r==R or c==C or (r,c) in visit or board[r][c] not in node.children):
                return 
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][]
            


# @lc code=end

