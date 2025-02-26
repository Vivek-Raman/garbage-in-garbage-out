from typing import List


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    fuel = 0
    for num in nums:
      if fuel < 0:
        return False
      if num > fuel:
        fuel = num
      fuel -= 1
    return True



if __name__ == '__main__':
  print(Solution().canJump([2,5,0,0]))
