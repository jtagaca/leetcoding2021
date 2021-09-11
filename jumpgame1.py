
#O(n)^n since for every element we have to consider n-1 elements 
# O(n) space before we start popping off the call stack
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def isPossible(nums,idx):
            if idx==len(nums)-1:
                return True
            for i in range(idx+1, nums[idx]+idx+1):
                output=isPossible(nums, i)
                if output== True:s
                    return True
            return False
            
            
        
        
        return isPossible(nums, 0)
        
            
        
#O(n) time and O(n) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal= len(nums)-1 
        for i in reversed(range(len(nums))):
            if i+nums[i]>=goal:
                goal=i
            
        return True if goal==0 else False
            
        
        