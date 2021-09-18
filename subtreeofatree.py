class Solution(object):
    
    #time is O(n*t) where n is the number of nodes in the 
    # root and the t is the number of nodes in the subtree
    # space complexity would be O(n+t) since at most we will traverse n+ t nodes
    def isSameTree(self, s, t):
        if not s and not t:
            return True

        if not s and t or s and not t:
            return False

        if s.val != t.val:
            return False

        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    
    # we first call ↓ and see that if the root node is the same as the node 
    # then for each node in the root node we check if this is the valid tree
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True

        res = self.isSameTree(s, t)
				
        if s.left:
            # once we have found the res as possible it will always be possitive 
            res = res or self.isSubtree(s.left, t)
        if s.right:
            res = res or self.isSubtree(s.right, t)
        return res