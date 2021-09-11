
#O(n!) time since we are vising each node at least once
#O(n) space complexity
def isPossible(index, map, jump):
    
    if index >= len(map): return True
    elif map[index] == 1: return False
    #we are checking if our neighbor is possible to be considered
    # 
    return isPossible(index + 1, map, jump) or isPossible(index + jump + 1, map, jump)

def isPossibleMain(map, jump):
	return isPossible(0, map, jump)
    		



array1=[0, 1, 0, 0, 0, 1, 1, 0, 1, 0]

print(isPossibleMain(array1, 2))