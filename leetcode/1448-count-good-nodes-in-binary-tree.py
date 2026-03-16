# 1448. Count Good Nodes in Binary Tree

from collections import deque
from utils.tree import TreeNode, from_level_order


class Solution:

  def goodNodes(self, root: TreeNode) -> int:
    if not root:
      return []

    good_nodes = 0

    stack = deque([(root, root.val)])
    while len(stack) > 0:
      node, max_so_far = stack.pop()

      if node.val >= max_so_far:
        good_nodes += 1
        # print(node.val)
        max_so_far = max(max_so_far, node.val)

      if node.left: stack.append((node.left, max_so_far))
      if node.right: stack.append((node.right, max_so_far))

    return good_nodes


if __name__ == "__main__":
  s = Solution().goodNodes(from_level_order([3, 1, 4, 3, None, 1, 5]))
  print(s)
