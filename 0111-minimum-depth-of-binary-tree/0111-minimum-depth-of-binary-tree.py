# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q = deque([(root,1)])
        
        while q:

            cur, level = q.popleft()

            if not cur.left and not cur.right:
                return level

            if cur.left:
                q.append((cur.left, level + 1))

            if cur.right:
                q.append((cur.right, level + 1))

   
        



        # def recursion(node):
        #     if not node:
        #         return 0
        #     if not node.left and not node.right:
        #         return 1
        #     left_depth = recursion(node.left)
        #     right_depth = recursion(node.right)
        #     if left_depth == 0 or right_depth == 0:
        #         return max(left_depth, right_depth) + 1
        #     return min(left_depth, right_depth) + 1

        # return recursion(root)

