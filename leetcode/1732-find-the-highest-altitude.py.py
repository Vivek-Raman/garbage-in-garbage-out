from typing import List


class Solution:

  def largestAltitude(self, gain: List[int]) -> int:
    highest = 0
    current = 0
    for g in gain:
      current += g
      if current > highest:
        highest = current
    return highest


if __name__ == "__main__":
  s = Solution().largestAltitude(gain = [-5,1,5,0,-7])
  print(s)
