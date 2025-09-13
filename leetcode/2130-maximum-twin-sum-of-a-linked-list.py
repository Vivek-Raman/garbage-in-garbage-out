class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return f'{self.val} --> {self.next.__str__()}'


from typing import Optional

class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    n = 0
    p1 = head
    while p1 is not None:
      n += 1
      p1 = p1.next

    p1 = head
    p2 = head.next
    p1.next = None
    for _ in range(n // 2 - 1):
      temp = p2.next
      p2.next = p1
      p1 = p2
      p2 = temp

    max_sum = -1
    for _ in range(n // 2):
      summed = p1.val + p2.val
      if max_sum < summed:
        max_sum = summed
      p1 = p1.next
      p2 = p2.next
    return max_sum

if __name__ == '__main__':
  print(Solution().pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))))
