# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        if not root:
            return 0


        q = deque([(root,1)])


        while q:

            cur, level = q.popleft()

            # if not cur.left or not cur.right:
            #     return level

            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))




        return level










        # def recursion(node):
        #     if not node:
        #         return 0
        #     left_depth = recursion(node.left)
        #     right_depth = recursion(node.right)
        #     depth = max(left_depth, right_depth) + 1
        #     return depth

        # return recursion(root)


        # answer = 0




        # def recursion(node,depth):
        #     nonlocal answer  

        #     if not node:
        #         return
                 
        #     cur_depth = depth + 1
        #     answer = max(answer, cur_depth)
        #     recursion(node.left, cur_depth)
        #     recursion(node.right, cur_depth)

        # recursion(root,0)
        # return answer




