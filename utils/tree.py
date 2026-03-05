from collections import deque
from typing import List, Optional


class TreeNode:

  def __init__(self,
               val=0,
               left: Optional[TreeNode] = None,
               right: Optional[TreeNode] = None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self) -> str:
    return str(to_level_order(self))


def from_level_order(arr: List[int], i: int = 0) -> TreeNode:
  # children of arr[n] will be at
  #   LEFT: arr[2 * n + 1]
  #   RIGHT: arr[2 * n + 2]
  l = len(arr)
  root = TreeNode(arr[i])

  idx_l = 2 * i + 1
  if idx_l < l and arr[idx_l] is not None:
    # left child exists
    root.left = from_level_order(arr, idx_l)

  idx_r = 2 * i + 2
  if idx_r < l and arr[idx_r] is not None:
    # left child exists
    root.right = from_level_order(arr, idx_r)

  return root


def to_level_order(root: TreeNode) -> List[int]:
  arr = []
  visited = deque[Optional[TreeNode]]([root])

  while len(visited) > 0:
    node = visited.popleft()
    if node is None:
      arr.append(None)
      continue
    arr.append(node.val)
    visited.append(node.left)
    visited.append(node.right)
  while arr[-1] is None:
    arr.pop()
  return arr


# if __name__ == '__main__':
#   arr = [5, 3, 6, 2, 4, None, 7]
#   test_tree = from_level_order(arr)
#   arr = to_level_order(test_tree)
#   print('Run 1: ', arr)
#   test_tree = from_level_order(arr)
#   arr = to_level_order(test_tree)
#   print('Run 2: ', arr)
