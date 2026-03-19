# 2352. Equal Row and Column Pairs

from collections import defaultdict
from typing import List


class Solution:

  def equalPairs(self, grid: List[List[int]]) -> int:
    if not grid or not grid[0]: return 0
    n = len(grid)

    rows = defaultdict(int)
    for i in range(n):
      row = []
      for j in range(n):
        row.append(grid[i][j])
      key = str(row)
      rows[key] += 1

    result = 0

    for j in range(n):
      row = []
      for i in range(n):
        row.append(grid[i][j])
      key = str(row)
      result += rows.get(key, 0)
      # rows[key] += 1

    return result


if __name__ == "__main__":
  # s = Solution().equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]])
  s = Solution().equalPairs(grid=[
      [3, 1, 2, 2],
      [1, 4, 4, 5],
      [2, 4, 2, 2],
      [2, 4, 2, 2],
  ])
  print(s)
