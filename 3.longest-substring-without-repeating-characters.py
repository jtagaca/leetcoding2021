# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        cset = set()

        for r in range(len(s)):
            # while there is something that
            # is the same as the value in cset
            # we keep popping and
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            res = max(res, r-l+1)
        return res


# @lc code=end
