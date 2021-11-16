#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start


#Time and space is O(n) and O(n) but the main thing is that it will be slow since we are having to pass at most 1000n because of the while loop
# space is because we have a set 
import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # how to keep adding values in a an array 
        # all positives 
        
        
        # set 
        # generate vals that in range of n-1 
            # not in the set 
            # appending array 
        # compute last val if to make up the dif on the total of n-1 to bring to zero
            # loop and add total
            # if val 
            # currentNumber= opposite(total -0)
            
        if n==1:
            return [0]
        
        values=set()
        output=[]
        total=0
        
        for i in range(1,n):
            valTobeAppended=random.randint(-1000,1000)
            while valTobeAppended in values or valTobeAppended ==0:
                valTobeAppended=random.randint(-500,500)
                
            output.append(valTobeAppended)
            values.add(valTobeAppended)
            total+=valTobeAppended
            
        # what if the total is 0 and 0 is already in the set 
        
        if total==0:
            output.append(0)
            
        else:
            currentVal= -1* total
            output.append(currentVal)
            
        return output
            
        
            
            
            
        
# @lc code=end

