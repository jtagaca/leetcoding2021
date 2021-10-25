# @before-stub-for-debug-begin


# @before-stub-for-debug-end

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
# import collections
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # empty input or len is 1 return [[""]] 
#         # create the hashmap key is sorted and value is list 
#         # output.append(vals)
        
#         # loop through the keys and append to output 
        
#         if len(strs)==0 or len(strs)==1:
#             return [strs]
        
#         hashm=collections.defaultdict(list)
#         for s in strs:
#             sortedlistS=sorted(s)
#             sorteds=("").join(sortedlistS)
#             hashm[sorteds].append(s)
            
#         output=[]
        
#         for key, val in hash.items():
#             output.append(val)
            
#         return output
            
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty input or len is 1 return [[""]] 
        # create the hashmap key is sorted and value is list 
        # output.append(vals)
        
        # loop through the keys and append to output 
        
        
       
        # loop through and find the values values of frequency for each character 
         # make temp list of 26 since a lower chars are 26 char available 
        # make this a key and append 
        #O(n *k) where n is the len of the given input and k is the len of the s
        # O(n*K) since we are storing an array of strings
        #an array of strings will always be O(n*k) space 
        hashm=collections.defaultdict(list)
        
        for s in strs:
            tempKey=[0] * 26
            
            for c in s:                 
                tempKey[ord(c)-ord('a')]+=1
            hashm[tuple(tempKey)].append(s)
            
        return hashm.values()
            
                
# @lc code=end

