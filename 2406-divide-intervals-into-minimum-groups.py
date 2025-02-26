from typing import List


class Solution:
  def minGroups(self, intervals: List[List[int]]) -> int:
    starts = []
    stops = []

    for interval in intervals:
      starts.append(interval[0])
      stops.append(interval[1])

    starts.sort()
    stops.sort()

    max_groups = 1
    groups = 0

    i = 0
    j = 0
    while i < len(starts) and j < len(intervals):
      if starts[i] <= stops[j]:
        groups += 1
        i += 1
      else:
        groups -= 1
        j += 1
      max_groups = max(max_groups, groups)

    return max_groups


if __name__ == '__main__':
  print(Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
