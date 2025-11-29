from functools import reduce
from typing import List


class Solution:

  def pivotIndex(self, nums: List[int]) -> int:
    left_sum = 0
    right_sum = reduce(lambda x, y: x + y, nums) - nums[0]
    if left_sum == right_sum:
      return 0

    for i in range(len(nums) - 1):
      left_sum += nums[i]
      right_sum -= nums[i + 1]
      print(left_sum, right_sum)
      if left_sum == right_sum:
        return i + 1
    return -1


if __name__ == "__main__":
  s = Solution().pivotIndex(nums=[2, 1, -1])
  # s = Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
  print(s)
