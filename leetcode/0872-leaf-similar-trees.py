from collections import deque
from typing import Optional
from utils.tree import TreeNode, from_level_order


class Solution:

  def findLeaves(self, root: TreeNode):
    leaves = []
    stack = deque[TreeNode]([root])
    while len(stack) > 0:
      node = stack.pop()
      if node.left is not None:
        stack.append(node.left)
      if node.right is not None:
        stack.append(node.right)
      if node.left is None and node.right is None:
        leaves.append(node.val)
    return leaves

  def leafSimilar(self, root1: Optional[TreeNode],
                  root2: Optional[TreeNode]) -> bool:
    leaves1 = self.findLeaves(root1)
    leaves2 = self.findLeaves(root2)
    # print(leaves1, leaves2)
    return leaves1 == leaves2


if __name__ == "__main__":
  s = Solution().leafSimilar(
      root1=from_level_order([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
      root2=from_level_order(
          [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]))
  print(s)
