# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        def dfs(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return(
                p.val==q.val
                and dfs(p.left,q.left)
                and dfs(p.right,q.right)
            )
        if dfs(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))