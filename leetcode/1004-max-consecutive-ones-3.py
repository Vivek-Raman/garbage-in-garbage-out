# 1004. Max Consecutive Ones 3

from typing import List


class Solution:

  def longestOnes(self, nums: List[int], k: int) -> int:
    max_ones = 0
    tally_ones = 0
    tally_zeroes = 0
    l = 0
    r = 0
    while r < len(nums):
      if nums[r] == 1:
        # print('inc R')
        tally_ones += 1
        r += 1
      elif nums[r] == 0 and tally_zeroes < k:
        # print('inc R - zero flipped')
        tally_zeroes += 1
        tally_ones += 1
        r += 1
      else:
        if nums[l] == 1:
          # print('no more flips - inc L')
          tally_ones -= 1
          l += 1
        else:
          # print('no more flips - inc L and regain flip')
          tally_zeroes -= 1
          tally_ones -= 1
          l += 1

      if tally_ones > max_ones:
        max_ones = tally_ones

    return max_ones


if __name__ == "__main__":
  # s = Solution().longestOnes(nums=[1, 0, 1, 0], k=0)
  s = Solution().longestOnes(
      nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0], k=3)
  print(s)
