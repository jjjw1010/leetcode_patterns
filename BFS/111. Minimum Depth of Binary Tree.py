# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # For invalid input
        if not root: return 0

        # Using Tuple for organization
        stack = deque([(root, 1)])
        # Iterate each node at a time instead of whole level at a time
        while stack:
            node, cur_level = stack.popleft()
            if node:
                if not node.left and not node.right:
                    return cur_level
                if node.left: stack.append((node.left, cur_level + 1))
                if node.right: stack.append((node.right, cur_level + 1))   