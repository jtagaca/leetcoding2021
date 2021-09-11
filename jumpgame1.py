
#O(n)^n since for every element we have to consider n-1 elements 
# O(n) space before we start popping off the call stack


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #we are checking every possible path that is available on every element ↓
        def isPossible(nums,idx):
            if idx==len(nums)-1:
                return True
            for i in range(idx+1, nums[idx]+idx+1):
                output=isPossible(nums, i)
                if output== True:
                    return True
            return False
            
            
        
        
        return isPossible(nums, 0)
        
            
        
#O(n) time and O(n) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal= len(nums)-1 
        # we have a goal and every time our goal is reachable by our left neighbor
        # then we know we can use that to be our current goal 
        # since we can reach our prev using that position
        
        for i in reversed(range(len(nums))):
            if i+nums[i]>=goal:
                goal=i
            
        return True if goal==0 else False
            
        
        