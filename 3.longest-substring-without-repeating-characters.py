class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input = string
        # int 
        # empty input 
        # longest substring that is present in the string that are unique 
        # O(n) and for space None 
        
        # abcsa"
        
         
        
        maxResult=0
        l,uniqueVal=0,set()
        for r in range(len(s)):
        # sliding window 
        # intialize a set 
        # if we see something in the the current position of the r 
            while s[r] in uniqueVal:
                uniqueVal.remove(s[l])
                l+=1
            uniqueVal.add(s[r])
            # update maxResult everytime if the new list is created 
            maxResult=max(maxResult,len(list(uniqueVal)))
            
        return maxResult
            
        
                
        
        
        
        
        
        
        
