# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            if key <node.val:
                node.left=dfs(node.left)

            elif key > node.val:
                node.right=dfs(node.right)
            else:

                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                temp=node.right

                while temp.left:
                    temp=temp.left

                node.val=temp.val
                node.right=self.deleteNode(node.right,temp.val)

            return node

        return dfs(root)

                
                    
               





        