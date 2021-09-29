class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # craft the permutation table?
        # find our current permutation then then check the next one 
        # this would require to generate permutation possible 
        # scale?
        # empty input 
        # a list 
        # int list 
        # what is a permutation 
        # the next value that is next to the given number 
        # time space of  O(1) for space
        
        # 15011
        # 3 2
        
        
        
        
        l,r=len(nums)-1,len(nums)-1
        
        
        # we are not in ascending any more 
        # as long as we are not in the start then we swap our left val with the val 
        while l>0 and nums[l-1]>=nums[l]:
            l-=1
        
        if l==0:
            nums.reverse()
            return nums
        k=l-1
        # that we first find in the right that is larger than us
        # reverse values from left+1 til the end of the array
        while nums[k]>=nums[r]:
            r-=1
        
        nums[k], nums[r] = nums[r], nums[k]
        r=len(nums)-1
        
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums
        
        
        
        
            
        
        
        
        
        
        
        
        
        