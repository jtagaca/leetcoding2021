class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        mostFarIDX=0
        result=0
        
        #time complexity of O(n) because we are visiting each element at least once 
        # space of O(1) because we are not using any extra space 
        
        # this works because each time we get the farthest using our current index 
        # then from here we shift left and right 
        # left will always be the next value to right before shifting right to the most farthest
        while r <len(nums)-1:
            # we are getting the mostFar value here 
            for i in range(l,r+1):
                mostFarIDX=max(mostFarIDX, nums[i]+i) 
            l=r+1
            r=mostFarIDX
            result+=1
        return result