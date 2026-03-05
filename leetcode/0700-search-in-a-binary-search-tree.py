# Definition for a binary tree node.
from typing import Optional


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

    def __str__(self) -> str:
      return f"{self.val},{str(self.left)},{str(self.right)}"


class Solution:

  def searchBST(self, root: Optional[TreeNode],
                val: int) -> Optional[TreeNode]:
    if root is None:
      return None
    if root.val == val:
      return root
    elif root.val > val:
      return self.searchBST(root.left, val)
    else:
      return self.searchBST(root.right, val)


if __name__ == "__main__":
  s = Solution().searchBST(
      TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2)
  print(s)
