from operator import xor
from typing import Optional, Tuple

from utils.tree import TreeNode, from_level_order


class Solution:

  def findNode(
      self,
      node: Optional[TreeNode],
      key: int,
      parent: Optional[TreeNode] = None
  ) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
    if node is None:
      return None, None
    elif key < node.val:
      return self.findNode(node.left, key, node)
    elif key > node.val:
      return self.findNode(node.right, key, node)
    elif key == node.val:
      return node, parent

  def deleteNode(self, root: Optional[TreeNode],
                 key: int) -> Optional[TreeNode]:
    to_delete, parent = self.findNode(root, key)
    # no node to delete
    if to_delete is None:
      return root
    # if parent is None:
    #   # deleting root element
    #   return None

    # TODO: if root node is updated / if parent is null

    is_right_of_parent = parent.right == to_delete

    left_none = to_delete.left is None
    right_none = to_delete.right is None

    # node has no children
    if left_none and right_none:
      if is_right_of_parent:
        parent.right = None
      else:
        parent.left = None

    # node has only left / right child
    elif xor(left_none, right_none):
      if not left_none:
        if is_right_of_parent:
          parent.right = to_delete.left
        else:
          parent.left = to_delete.left
      else:
        if is_right_of_parent:
          parent.right = to_delete.right
        else:
          parent.left = to_delete.right

    # node has both children
    else:
      if is_right_of_parent:
        # find successor
        successor_node = to_delete.right
        successor_parent = to_delete
        while successor_node.left is not None:
          successor_parent = successor_node
          successor_node = successor_node.left
        to_delete.val = successor_node.val
        root = self.deleteNode(successor_parent, successor_node.val)
      else:
        # find predecessor
        predecessor_node = to_delete.left
        predecessor_parent = to_delete
        while predecessor_node.right is not None:
          predecessor_parent = predecessor_node
          predecessor_node = predecessor_node.right
        to_delete.val = predecessor_node.val
        root = self.deleteNode(predecessor_parent, predecessor_node.val)

    return root


if __name__ == "__main__":
  # t = from_level_order([5, 3, 6, 2, 4, None, 7])
  # print('CASE: Nothing to delete: ', t)
  # s = Solution().deleteNode(t, 9)
  # print('CASE: Nothing to delete: ', s)
  # print()

  # t = from_level_order([5, 3, 6, 2, 4, None, 7])
  # print('CASE: No child node(s): ', t)
  # s = Solution().deleteNode(t, 2)
  # print('CASE: No child node(s): ', s)
  # print()

  # t = from_level_order([5, 3, 6, 2, None, None, 7])
  # print('CASE: 1L child node(s): ', t)
  # s = Solution().deleteNode(t, 3)
  # print('CASE: 1L child node(s): ', s)
  # print()

  # t = from_level_order([5, 3, 6, None, 4, None, 7])
  # print('CASE: 1R child node(s): ', t)
  # s = Solution().deleteNode(t, 3)
  # print('CASE: 1R child node(s): ', s)
  # print()

  # t = from_level_order([5, 3, 6, 2, 4, None, 7])
  # print('CASE:  2 child node(s): ', t)
  # s = Solution().deleteNode(t, 3)
  # print('CASE:  2 child node(s): ', s)
  # print()

  # t = from_level_order([0])
  # print('CASE:  Root only: ', t)
  # s = Solution().deleteNode(t, 0)
  # print('CASE:  Root only: ', s)
  # print()

  t = from_level_order([5, 3, 6, 2, 4, None, 7])
  print('CASE:  Fail: ', t)
  s = Solution().deleteNode(t, 3)
  print('CASE:  Fail: ', s)
  print()
