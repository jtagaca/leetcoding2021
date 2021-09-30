class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # THis will run on O(n) average and O(n^2) for worst case and this will have a space of 
        # O(1) because we are not using extra memory 
        # this works because we either find 1 and 0 for our left and right or it's 0 and 1 
        # then from here we expand 
        
        
        #matching 
        # expand 
        # match 1 and 0
        # add 1 
        # match 0 and 1 
        # add1 
        
        # "10101"
        count=0
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]=="1" and s[r]=="0":
                count+=1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]=="0"and s[r]=="1":
                count+=1
                l-=1
                r+=1
        return count
        
        