# 199. Binary Tree Right Side View

from collections import deque
from typing import List, Optional
from utils.tree import TreeNode, from_level_order


class Solution:

  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None: return []

    rightmost_by_level = {
        0: root,
    }

    q = deque([(root, 0)])
    while len(q) > 0:
      node, level = q.popleft()

      if node.left is not None:
        q.append((node.left, level + 1))
      if node.right is not None:
        q.append((node.right, level + 1))
      rightmost_by_level[level] = node.val

    return list(rightmost_by_level.values())


if __name__ == "__main__":
  s = Solution().rightSideView(from_level_order([1, 2, 3, None, 5, None, 4]))
  print(s)
