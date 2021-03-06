"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

visited =set()


# Time Complexity(DFS)

#https://stackoverflow.com/questions/1286751/difference-between-vertices-and-edges-graphs-algorithm-and-ds

# Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E), where V is the number of vertices and E is the number of edges. In case of DFS on a tree, the time complexity is O(V), where V is the number of nodes.

#O(n+m) where n is the number of nodes and m is the number of edges 
# O(n) where since we are storing at most n nodes in the hashmap 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # deep copy 
        # dfs 
        # we have to visit if not visited 
        
        # looping through every node that is in the neighbor and then 
        # append to nodes neighbor 
        
        # create node 
        # add to visited 
        # loop for every neighbor
            # node.neighbors add neighbor 
            # if not in visited call function
        
        # finish 
        
        if node is None:
            return node 
        
        
        
        return self.buildNodes(node)
    
    def buildNodes(self,node):
        global visited
        currentNode= Node(node.val,[])
        
        visited.add(node)
        
        for neighbor in node.neighbors:
            currentNode.neighbors.append(neighbor)
            if neighbor not in visited:
                self.buildNodes(neighbor)
                
        return currentNode
            