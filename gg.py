class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merger helper fn 
        # if even len then i=n//2 + i+i
        # float? 
        # o(klogk) where k is the combined len of list 1 and list 2 
        # space: o(k) where k is the combined len of list 1 and list 2 
        
        # new time complexity is O(k) and O(k) for space 
        copy=self.sortArray(nums1,nums2)

        
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
    
    def sortArray(self,nums1,nums2):
        temp=[]
        i=j=0
        while i< len(nums1) and j< len(nums2):
            curNum1=nums1[i]
            curNum2=nums2[j]
            
            if curNum1<curNum2:
                temp.append(curNum1)
                i+=1
            else:
                temp.append(curNum2)
                j+=1
        if j==len(nums2):
            temp.extend(nums1[i:])
        else:
            temp.extend(nums2[j:])
        
        return temp 
        