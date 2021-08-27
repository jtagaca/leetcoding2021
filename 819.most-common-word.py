# @before-stub-for-debug-begin
from python3problem819 import *
from typing import *
from collections import defaultdict
# @before-stub-for-debug-end

#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalWord = "".join(
            [c.lower() if c.isalnum() else " " for c in paragraph])
        splittedWord = normalWord.split()
        banned_words = set(banned)
        hashm = DefaultDict(int)
        for word in splittedWord:
            if word not in banned_words:
                hashm[word] += 1
        maxFreq = max(hashm.items(), key=lambda x: x[1])
        return maxFreq[0]

# @lc code=end
