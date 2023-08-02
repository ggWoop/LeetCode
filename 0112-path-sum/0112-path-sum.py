# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        if not root:
            return 0


        q = deque([(root,0)])
        answer = 0
        while q:

            cur , cur_sum = q.popleft()
            cur_sum += cur.val
            if not cur.left and not cur.right and cur_sum == targetSum:
                return True


            if cur.left:
                q.append((cur.left, cur_sum ))
                
            if cur.right:
                q.append((cur.right, cur_sum ))




        return False






