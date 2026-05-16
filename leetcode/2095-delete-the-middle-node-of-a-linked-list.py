# 2095. Delete the Middle Node of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from utils import ListNode


class Solution:

  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
      return None
    fast = head
    slow = head
    pre_slow = head
    while fast and fast.next:
      pre_slow = slow
      slow = slow.next
      fast = fast.next.next

    if slow.next:
      pre_slow.next = ListNode(slow.next.val, slow.next.next)
    else:
      pre_slow.next = None
    return head


if __name__ == "__main__":
  s = Solution().deleteMiddle([1, 3, 4, 7, 1, 2, 6])
  print(s)
