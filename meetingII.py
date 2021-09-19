class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sorting via the first number? 
        # sort by the second number 
        # currenttotal for overflow 
        # stack  
        # we return the len of stack
        # we only append if currentstart is lessthan the stackend 
        start=[]
        end=[]
        
        for startv, endv in intervals:
            start.append(startv)
            end.append(endv)
        start.sort()
        end.sort()
        
        # this is basically saying in point in time 
        # are there a meeting that is currently happening?
        # and at that time we are incrementing the value by one 
        
        s,e=0,0
        count=0
        res=float('-inf')
        while s< len(start):
            if start[s]<end[e]:
                #something is starting                
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res=max(res, count)
            
        return res
            
                
            
        
        
        
        
        
        
        