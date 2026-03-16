# 1161. Maximum Level Sum of a Binary Tree

from collections import defaultdict, deque
from typing import Optional
from utils.tree import TreeNode, from_level_order


class Solution:

  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    if root is None: return 0

    level_sum = defaultdict[int, int](lambda: 0)

    q = deque([(root, 1)])
    while len(q) > 0:
      node, level = q.popleft()
      level_sum[level] += node.val
      if node.left:
        q.append((node.left, level + 1))
      if node.right:
        q.append((node.right, level + 1))

    max_level = 1
    max_sum = level_sum[max_level]
    for level, sum in level_sum.items():
      if sum > max_sum:
        max_sum = sum
        max_level = level
    return max_level


if __name__ == "__main__":
  s = Solution().maxLevelSum(from_level_order([1, 7, 0, 7, -8, None, None]))
  print(s)
