# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val


#         self.next = next
from typing import Optional

from linkedlist.linkedlist_reverse import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # printing the middle of a linked list?
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    middle = solution.middleNode(head)
    print(f"Middle node value: {middle.val}")  # Output: 3
