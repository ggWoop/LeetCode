"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        answer = 0
        if not root:
            return answer

        q = deque([(root,1)])

        while q:

            cur, level = q.popleft()

            answer = max(answer,level)

            if cur.children:
                for i in cur.children:
                    q.append((i,level + 1))
                

        return answer

        