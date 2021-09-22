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
        self.children = {}
        self.isEnd = False
    # we mark the the end of the word by ading a boolean value of isWord
    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEnd = True

# time complexity would be O(mn * 4 ^ m*n) where n is the len of the board and m is the width of the board 
# O(l) where l is the len of the longest word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # adding nodes
        root = TrieNode()
        # creating the trienodes and the end will have a marker of isEnd
        for w in words:
            root.addWord(w)

        # we perform the traversal
        def dfs(r, c, node, word):
            nonlocal visit, board
            # if it's out of bounds or it has been visited in this cycle then we do not consider it as well as if it is not present in our node hashmap
            # we see that it is actually one of our current start node or value 
            if (r < 0 or c < 0 or r == R or c == C or (r, c) in visit or board[r][c] not in node.children):
                return
            #try and see if ↓ will be able to hit the base case 
            visit.add((r, c))
            node = node.children[board[r][c]] # repointing node here 
            word += board[r][c]

            
            # if this node is the end of the word then we have found it 
            if node.isEnd:
                res.add(word)
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r, c))
        R, C = len(board), len(board[0])
        res, visit = set(), set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                # first we wil try to see if this is a valid start 
                # if it does then we use our trie structure to see if it would be possible 
                # if it doesn't work out then we can always remove the colateral using the .remove()
                dfs(r, c, root, "")

        return list(res)


# @lc code=end
