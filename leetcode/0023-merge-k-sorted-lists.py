# 23. Merge k Sorted Lists

from collections import defaultdict
from typing import List, Optional


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    s = str(self.val)
    if self.next is not None:
      s += f", {str(self.next)}"
    return s


class Solution:

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res = None
    p = None

    while True:
      min_node = None
      min_node_idx = -1
      for i in range(len(lists)):
        node = lists[i]
        if node is None: continue
        if min_node is None or node.val < min_node.val:
          min_node = node
          min_node_idx = i

      if min_node is None: break

      # insert
      if not res:
        res = ListNode(min_node.val)
        p = res
      else:
        p.next = ListNode(min_node.val)
        p = p.next

      # progress head
      if lists[min_node_idx] is not None:
        lists[min_node_idx] = lists[min_node_idx].next

    return res


if __name__ == "__main__":
  s = Solution().mergeKLists(lists=[
      ListNode(1),
      ListNode(0),
  ])
  print(s)
