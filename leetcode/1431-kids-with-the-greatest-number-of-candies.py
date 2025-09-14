from functools import reduce
from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    res = []
    max = reduce(lambda x,y: x if x > y else y, candies);
    for candy in candies:
      res.append(candy + extraCandies >= max)
    return res


if __name__ == '__main__':
  s = Solution().kidsWithCandies([2,3,5,1,3], 3)
  print(s)
