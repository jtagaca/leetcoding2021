class Solution:
    def validPalindrome(self, string: str) -> bool:
        # deleting one only
        # do we always need to delete one or could this be optional?
        # output true or false not a string
        # do we have a time and space constraint for her?
        # hashmap 
        # frequency does not matter position does
        # check what letter could we remove
        # if how many were different is two were different then we know that we cannot do the #valid palindrome
        # aabbbab
        # pair 
        # we need to move just one pointer if they are not the same
        # counter should still have the number of difference 
        
       #O(n) time 
        
       # either one would work? 
    # we check possibilities of l and righ if they are not the same 
    # we check if either possibilities would work
        l, r = 0, len(string)-1
        total=0
         #l r 
        while l < r:
            # move l if not the same run the loop again
            # increment counter if not the same
            if string[l]!=string[r]:
                if self.ValidPal(l+1, r,string) or self.ValidPal(l,r-1,string):
                    return True
                else:
                    return False
            
             # else l+=1 r -=1
            else:
                l+=1
                r-=1
        return True
    # ccbba
    def ValidPal(self,l, r, string):
        if l==r:
            return True
        while l<r:
            if string[l]!=string[r]:
                return False
            else:
                l+=1
                r-=1
        return True 
        
        
        