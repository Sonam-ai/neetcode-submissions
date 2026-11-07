# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Store inorder value -> index
        inorder_map = {}

        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        preIndex = 0

        def helper(left, right):
            nonlocal preIndex

            # Base case: no elements
            if left > right:
                return None

            # First element in preorder is root
            root_val = preorder[preIndex]
            preIndex += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left subtree
            root.left = helper(left, mid - 1)

            # Build right subtree
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
        