# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        answer = 0
        if not root:
            return answer
        
        from collections import deque, defaultdict

        q = deque([(root, 0)])
        d = defaultdict(int)
        while q:
            cur_node, level = q.popleft()
            d[level] += cur_node.val
            if cur_node.left:
                q.append((cur_node.left, level + 1))
            if cur_node.right:
                q.append((cur_node.right, level + 1))
        
        return d[max(d.keys())]

