from collections import deque
from typing import Optional


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def recurse(self, node: TreeNode, depth: int) -> int:
    if node.left is None and node.right is None:
      return depth

    depth_l = depth
    depth_r = depth
    if node.left is not None:
      depth_l = self.recurse(node.left, depth + 1)
    if node.right is not None:
      depth_r = self.recurse(node.right, depth + 1)
    return max(depth_l, depth_r)

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0
    return self.recurse(root, 1)


if __name__ == "__main__":
  # s = Solution().maxDepth(
  #     TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
  s = Solution().maxDepth(TreeNode(1, None, TreeNode(2)))
  print(s)
