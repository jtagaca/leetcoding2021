#[-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #hashmap 
        #splicing 
        #
        # 
        currentMaxSubarray= nums[0]
        globalMaxSubarray=nums[0]
        
        for num in nums[1:]:
            currentMaxSubarray= max(num, currentMaxSubarray+num)
            globalMaxSubarray=max(currentMaxSubarray, globalMaxSubarray)
            
        return globalMaxSubarray
        
        