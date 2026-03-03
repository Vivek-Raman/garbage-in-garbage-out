from typing import List


class Solution:

  def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_avg = -999999
    run_avg = 0.0
    l = 0
    r = 0
    n = len(nums)
    print(n)
    while r < n:
      run_avg += nums[r] / k
      # print(f"adding {nums[r]}")
      if r >= k:
        run_avg -= nums[l] / k
        # print(f"remove {nums[l]}")
        l += 1
      if r >= k - 1:
        max_avg = max(max_avg, run_avg)
      # print(f"run: {run_avg}, max: {max_avg}")
      r += 1
    return max_avg


if __name__ == "__main__":
  # s = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
  # s = Solution().findMaxAverage(nums=[5], k=1)
  s = Solution().findMaxAverage(nums=[
      -6662,
      5432,
      -8558,
      -8935,
      8731,
      -3083,
      4115,
      9931,
      -4006,
      -3284,
      -3024,
      1714,
      -2825,
      -2374,
      -2750,
      -959,
      6516,
      9356,
      8040,
      -2169,
      -9490,
      -3068,
      6299,
      7823,
      -9767,
      5751,
      -7897,
      6680,
      -1293,
      -3486,
      -6785,
      6337,
      -9158,
      -4183,
      6240,
      -2846,
      -2588,
      -5458,
      -9576,
      -1501,
      -908,
      -5477,
      7596,
      -8863,
      -4088,
      7922,
      8231,
      -4928,
      7636,
      -3994,
      -243,
      -1327,
      8425,
      -3468,
      -4218,
      -364,
      4257,
      5690,
      1035,
      6217,
      8880,
      4127,
      -6299,
      -1831,
      2854,
      -4498,
      -6983,
      -677,
      2216,
      -1938,
      3348,
      4099,
      3591,
      9076,
      942,
      4571,
      -4200,
      7271,
      -6920,
      -1886,
      662,
      7844,
      3658,
      -6562,
      -2106,
      -296,
      -3280,
      8909,
      -8352,
      -9413,
      3513,
      1352,
      -8825,
  ],
                                k=90)
  print(s)
