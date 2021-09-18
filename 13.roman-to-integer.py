#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hashm = {
            'I' : 1,
            'IV':4,
            'V' : 5,
            'IX':9,
            'X' : 10,
            'XL':40,
            'L' : 50,
            'XC':90,
            'C' : 100,
            'CD':400,
            'D' : 500,
            'CM':900,
            'M' : 1000
        }
        
        #if we see our right is more than us then this might be a special value 
        # if right is bigger then we know that we need both values to get the true val
        # we keep adding 
        i=0
        total=0
        while i< (len(s)):
            #if we have a right neighbor
            print(i)
            if i+1<len(s):
                neigh=i+1
            # we are perfoming a check if our currentRoman is less than our neigh:
            
            if neigh and hashm[s[i]]<hashm[s[neigh]]:
                print(neigh)
                currentRoman=s[i]+s[neigh]
                i=neigh+1
                print(i)
            else:
                currentRoman=s[i]
                i+=1
                
            total+=hashm[currentRoman]
            print(total)
            neigh=None
        return total
                
            
            
        
        
        
        
        
        
# @lc code=end

