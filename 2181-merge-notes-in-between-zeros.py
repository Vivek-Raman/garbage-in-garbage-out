from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode(0, None)
        sum_iterator = sum_head
        iterator = head
        while iterator is not None:
            if iterator.val == 0 and iterator.next is not None:
                sum_iterator.next = ListNode(0, None)
                sum_iterator = sum_iterator.next
            else:
                sum_iterator.val += iterator.val
            iterator = iterator.next
        return sum_head.next


if __name__ == '__main__':
    result = Solution().mergeNodes(ListNode(0, ListNode(2, ListNode(3, ListNode(0, None)))))
    print(result)
