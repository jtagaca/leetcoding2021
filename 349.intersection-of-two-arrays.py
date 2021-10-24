#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # set 
        # itersection is the same number in both arrays 
        # create a sets 
        # use the min array after setting it to set to loop through and find the intersection 
        # if val for minimum list in longer list then append to output
        # empty input 
        # one number 
        
        
        # O(n+m) since we are converting to a set converting to a set is O(n) always even though we are trying to optimize using a min value  
        # space(n+m) 
        
        
        if len(nums1)<=0 or len(nums2)<=0:
            return None 
        tempSet1=set(nums1)
        tempSet2=set(nums2)
        
        minArrayOutput=list(tempSet1), tempSet2 if len(list(tempSet1)) < len(list(tempSet2)) else list(tempSet2), tempSet1
        minArray, maxSet= minArrayOutput[0], minArrayOutput[1]
        
        
        
        output=[]

        
        for val in minArray:
            if val in maxSet:
                output.append(val)
                
        return output
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

