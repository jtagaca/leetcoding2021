class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merger helper fn 
        # if even len then i=n//2 + i+i
        # float? 
        # o(klogk) where k is the combined len of list 1 and list 2 
        # space: o(k) where k is the combined len of list 1 and list 2 
        copy=list()
        copy.extend(nums1)
        copy.extend(nums2)

        copy.sort()
        curlen= len(copy)
        print(curlen)
        o=None
        middle=curlen//2
        if curlen %2 ==0 : 
            nextN=middle-1
            o=float(copy[middle]+copy[nextN])/2
        else: 
            o=float(copy[middle])
            
        return o 
        