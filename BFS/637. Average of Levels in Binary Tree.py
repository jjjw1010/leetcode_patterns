# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = deque([root])
        ans = []
        while stack:
            # Pop stack
            total = 0
            stack_len = len(stack)
            for _ in range(stack_len):
                node = stack.popleft()
                total += node.val
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            ans.append(total/stack_len)
        return ans