# @before-stub-for-debug-begin
from python3problem127 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import collections

# use math when it is difficult to explain time and space

# space would be #O(m^2 * n)
# time would be O(m^2 * n)because we are iterating at most
# O (m^2 * n)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build hashmap
        # do we have distinct values?
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        hashm = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # *ey use as key
                pattern = word[:i]+"*"+word[i+1:]
                hashm[pattern].append(word)
        q = [beginWord]
        res = 1
        visited = set([beginWord])
        while q:
            # use current
            # this is a way to keep track of the level that
            # we are in
            # so if we find a word
            # we check if this word is it
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                # get all the neighbors and append
                # we then check what charater
                # can we replace in order
                # to get closer to our endWord
                # for each time we consider our neighbors
                # because the neighbors will enable to reach the
                # endWord one way or another
                # if we do not find it then we just return 0

                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for neighbor in hashm[pattern]:
                        if neighbor not in visited:
                            # we only visit each word
                            # at least once because we have
                            # the visited
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1

        return 0
        # now traverse

        # perform bfs
        # increment res each time we remove
        # @lc code=end
