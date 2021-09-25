# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        # we are doing the palindrome but we are checking if it's a alpha numeric or 
        # if this is truee then we need to find the next character 
        # we need to check if our left and right are equal if not then it's palindrome
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
        
# @lc code=end

