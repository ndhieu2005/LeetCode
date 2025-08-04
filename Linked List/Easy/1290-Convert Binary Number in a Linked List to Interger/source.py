# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res,cur = 0,head
        while cur:
            res = (res<<1) +cur.val
            cur = cur.next
        return res


        