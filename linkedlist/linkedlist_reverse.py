# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next  # save next
            curr.next = prev  # reverse the pointers
            prev = curr  # move previous pointer
            curr = nxt  # move curr pointer
        return prev


# done using the prev and next pointers make sure to solve again the reverse of the pointers making the links reverse
