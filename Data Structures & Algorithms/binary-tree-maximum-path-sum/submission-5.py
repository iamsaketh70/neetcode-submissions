# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node):
        if not node:
            return 0
        leftsum = self.dfs(node.left)
        if leftsum<0:
            leftsum = 0
        rightsum = self.dfs(node.right)
        if rightsum<0:
            rightsum = 0
        self.maxsum  = max(self.maxsum,leftsum+rightsum+node.val)
        return max(leftsum,rightsum) + node.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        self.dfs(root)
        return self.maxsum