# 49. Group Anagrams

from collections import Counter, defaultdict
from typing import List


class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    letterset_to_group = defaultdict(list)
    sorted_strs = ["".join(sorted(s)) for s in strs]
    for i in range(len(strs)):
      letterset_to_group[sorted_strs[i]].append(strs[i])
    return [x for x in letterset_to_group.values()]

  def groupAnagrams_naive(self, strs: List[str]) -> List[List[str]]:
    strs.sort(key=len)

    res = []
    for i in range(len(strs)):
      l = strs[i]
      if l is None: continue
      len_l = len(l)
      count_l = Counter(l)
      group = [l]
      for j in range(i + 1, len(strs)):
        r = strs[j]
        if r is None: continue
        if len(r) != len_l: break
        count_r = Counter(r)
        if count_l == count_r:
          strs[j] = None
          group.append(r)
      res.append(group)
    return res


if __name__ == "__main__":
  # s = Solution().groupAnagrams(["asd", "sda"])
  s = Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
  print(s)
