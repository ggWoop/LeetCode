# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        cur = head

        word_list = []

        while cur:
            word_list.append(str(cur.val))
            cur= cur.next

        if word_list == word_list[::-1]:
            return True
        else:
            return False













