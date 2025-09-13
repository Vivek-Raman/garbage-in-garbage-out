from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summed = ListNode()
        summed_iter = summed
        while l1 is not None and l2 is not None:
            added = summed_iter.val + l1.val + l2.val
            summed_iter.val = added % 10
            if added >= 10:
                summed_iter.next = ListNode(added // 10)
            elif l1.next is not None or l2.next is not None:
                summed_iter.next = ListNode()
            summed_iter = summed_iter.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            added = summed_iter.val + l1.val
            summed_iter.val = added % 10
            if added >= 10:
                summed_iter.next = ListNode(added // 10)
            elif l1.next is not None:
                summed_iter.next = ListNode()
            summed_iter = summed_iter.next
            l1 = l1.next
        while l2 is not None:
            added = summed_iter.val + l2.val
            summed_iter.val = added % 10
            if added >= 10:
                summed_iter.next = ListNode(added // 10)
            elif l2.next is not None:
                summed_iter.next = ListNode()
            summed_iter = summed_iter.next
            l2 = l2.next
        return summed


if __name__ == '__main__':
    result = Solution().addTwoNumbers(ListNode(1, ListNode(8)),
                                      ListNode(0))
    print(result)
