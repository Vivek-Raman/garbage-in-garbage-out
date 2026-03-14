# 207. Course Schedule

from collections import defaultdict
from typing import Dict, List, Set


class Solution:

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    if len(prerequisites) == 0:
      return True

    graph = defaultdict(list)
    for [course, prereq] in prerequisites:
      graph[course].append(prereq)
    print(graph)

    def dfs(the_graph: Dict[int, List[int]], node: int,
            visited: Set[int]) -> bool:
      if node in visited:
        return len(the_graph[node]) == 0
      visited.add(node)

      adjacents = the_graph[node]
      if len(adjacents) == 0:
        return True
      else:
        for adj in adjacents:
          can_complete_prereq = dfs(the_graph, adj, visited)
          if not can_complete_prereq:
            return False
        the_graph[node] = []
      return True

    visited = set()
    for key in list(graph.keys()):
      if dfs(graph, key, visited) == False:
        return False
    return True


if __name__ == "__main__":
  s = Solution().canFinish(numCourses=20,
                           prerequisites=[[0, 10], [3, 18], [5, 5], [6, 11],
                                          [11, 14], [13, 1], [15, 1], [17, 4]])
  print(s)
