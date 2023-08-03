# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

       

        answer = 0
        if not root:
            return answer
        
        from collections import deque, defaultdict

        q = deque([(root, False)])
        while q:
            cur_node, is_left = q.popleft()
            if not cur_node.left and not cur_node.right and is_left:
                        answer += cur_node.val
            # 만약 현재 노드가 왼쪽, 오른쪽 자식이 모두 없고, is_left가 True 라면 answer에 cur_node.val를 더해줄 것
            if cur_node.left:
                q.append((cur_node.left, True))
            if cur_node.right:
                q.append((cur_node.right, False))
        return answer