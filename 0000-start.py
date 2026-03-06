from collections import deque
from typing import Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return f'{self.val},{self.next}'


class Solution:

  def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
      return head

    stack = deque[ListNode]()
    p = head
    while p is not None:
      stack.append(p)
      p = p.next
    rev_head = stack.pop()
    q = rev_head
    while len(stack) > 0:
      temp = stack.pop()
      q.next = temp
      q = q.next
    q.next = None

    return rev_head

  def reverseList_recur(self, head: Optional[ListNode],
                        ptr: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
      return head

    next_node = self.reverseList_recur(head.next)
    next_node.next

    while len(stack) > 0:
      temp = stack.pop()
      q.next = temp
      q = q.next
    q.next = None

    return rev_head

  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    return self.reverseList_recur(head, ListNode())


if __name__ == "__main__":
  s = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3,
                                                              ListNode(4)))))
  print(s)
