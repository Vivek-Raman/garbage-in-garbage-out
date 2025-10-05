from typing import List
from collections import Counter

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    c = Counter(arr)
    cc = Counter(c.values())
    for count in cc.values():
      if count > 1:
        return False
    return True



if __name__ == "__main__":
  s = Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
  print(s)
