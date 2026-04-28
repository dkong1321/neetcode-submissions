# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            # base case where we have no root
            if not root:
                return 0
            
            # recurse through the left and rightnodes
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # update the left and right if the max was negative take 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute the max path WITH spilt
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
        