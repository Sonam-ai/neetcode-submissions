# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q=collections.deque()
        q.append(root)
        result=[]
        while q:
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if i==0:
                    result.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return result

        