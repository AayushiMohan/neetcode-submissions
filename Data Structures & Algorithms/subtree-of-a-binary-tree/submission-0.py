class Solution:
    def isSubtree(self, root, subRoot):
        
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p, q):
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))