from typing import List


class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = dict()
    def compute(index: int, total: int) -> int:
      if index == len(nums):
        return 1 if target == total else 0
      if ((index, total) in dp):
        return dp[(index, total)]

      val = compute(index + 1, total + nums[index]) + compute(index + 1, total - nums[index])
      dp[(index, total)] = val
      return val

    return compute(0, 0)


if __name__ == '__main__':
  print(Solution().findTargetSumWays([1,1,1,1,1], 3))
