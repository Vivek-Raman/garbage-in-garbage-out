from typing import Optional
from utils.tree import TreeNode, from_level_order


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
  s = Solution().searchBST(from_level_order([5, 3, 6, 2, 4, None, 7], 2))
  print(s)
