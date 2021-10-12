#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        
        # O(n*m (n+m)) for time 
        # O(n*m) for space 
        
         
        # empty 
        # mutated matrix 
        
        # find the zero 
            # array 
            # loop through and if zero then add
        # convert row to 0 
            # for every val in arry
                # we use row at the same col 
            #   for 0 -> len(matrix)-1
                # we use col at the same row
            #   for 0 -> len(matrix[0])-1
                
        # convert col to 0 
        
        # if len(matrix)==0:
        #     return []
        
        # array=[]
        # # only have one checker for row and checker for col 
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c]==0:
        #             array.append((r,c))
        
        # while array:
        #     current=array.pop()
        #     tempr,tempc=current
            
        #     for r in range(len(matrix)):
        #         if matrix[r][tempc]==0:
        #             continue
        #         matrix[r][tempc]=0
        #     for c in range(len(matrix[0])):
        #         if matrix[tempr][c]==0:
        #             continue
        #         matrix[tempr][c]=0
    
        # return matrix 
        
        # row and column 
        
        
        # time O(m*n)
        # this will have a space of O(m+ n )
        # where m is the height of the matrix 
        # where n is the width of the matrix 
        rows, cols = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    r.add(r)
                    c.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c]=0
                    
                    
        return matrix
                    
        
                
                
            
        
        
        
        # return matr
# @lc code=end

