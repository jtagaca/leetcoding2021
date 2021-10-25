# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

#Time O(n^3) because we have a nested loop that is dependent on n and we have to check if they are a palindrome 
#Space (n) where n is the len of the given string
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # sliding window 
#         # helper func for palindrome 
#         # one letter word is a palindrome 
#         # n^3 brute force 
#         # set? 
#         # 
        
#         # a current char is a palindrome itself 
#         # maxPal= ""
#         # for char
#             # current pal
#         #   for current char til end 
#                 #currentpal.append(current)
#                 #if the len of current pal is > maxPal
#                     #check if palindrome
#                      # update maxpal join the array and update
        
        
        
#         if len(s)==0 or len(s)==1:
#             return s
        
#         maxPal=""
#         for i in range(len(s)):
#             currentpal=[]
#             curIDX=i
#             while curIDX<len(s):
#                 currentpal.append(s[curIDX])
#                 if len(currentpal) > len(maxPal) and self.isPalindrome(currentpal):
#                     maxPal=("").join(currentpal)
#                 curIDX+=1
                    
#         return maxPal
    
#     def isPalindrome(self, palindrome):
#         if len(palindrome)==1:
#             return True
#         l,r=0,len(palindrome)-1
        
#         while l <r:
#             if palindrome[l]!=palindrome[r]:
#                 return False
#             l+=1
#             r-=1
#         return True
        
def expand_and_count(s, start, end):
    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
        start -= 1
        end += 1
        
    # The indices used for the below substring are:
    # start + 1: because we kept decreasing start by 1 before breaking the loop
    # end: because we kept increasing end by 1 before breaking the loop
    # and python substring excludes the end index
    return s[start + 1 : end]

class Solution(object):
    def longestPalindrome(self, s):
# palindrome check on the middle 
# if we are in bounds and we are the same thing then keep decrementing and going up 
# return string[l+1, r]

#expanding on odd 
# expanding on even

# comparing which to use to update longest, longest will only be updated with the a longer value that is longer than longest
# return longest 
        
        #O(n^2) time because we are only at most either choosing odd or even at each time 
        #O(1) space 
        longest=''
        for i in range(len(s)):
            odd=self.expand(s,i,i)
            even=self.expand(s,i,i+1)

            longer=odd if len(odd)>len(even) else even

            if len(longer)>len(longest):
                longest=longer
        return longest
    
    def expand(self,string,left,right):
        while left>=0 and right<len(string) and string[left]==string[right]:
            left-=1
            right+=1
        return string[left+1: right]
     
        
        
        
      
    
                    
                
            
            
        
        
        
        
        
        
        
            
# @lc code=end

