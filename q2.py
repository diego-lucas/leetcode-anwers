from typing import Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        buffer = 0
        head = None

        while l1 or l2 or buffer:

            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            value, buffer = self.sum(buffer, val_l1, val_l2)
            if not head:
                head = ListNode(val=value)
                atual = head
            else:
                atual.next = ListNode(val=value)
                atual = atual.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head
        

    def sum(self, buffer: int, n1: int, n2: int) -> Tuple[int, int]:
        result = n1 + n2 + buffer
        buffer = 0
        if result > 9:
            buffer = result // 10
            result %= 10
        return result, buffer
