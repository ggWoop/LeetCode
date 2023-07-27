# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        cur = head
        answer = ""

        while cur:
            answer = answer + str(cur.val)
            cur = cur.next
        
        
        return int(answer, 2)