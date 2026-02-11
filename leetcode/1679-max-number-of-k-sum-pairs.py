from typing import List


class Solution:

  def maxOperationsV1(self, nums: List[int], k: int) -> int:
    i = 0
    n = len(nums)
    ans = 0
    for i in range(n):
      one = nums[i]
      if one == 0:
        continue
      for j in range(i + 1, n):
        two = nums[j]
        if two == 0:
          continue
        if one + two != k:
          continue
        ans += 1
        nums[i] = 0
        nums[j] = 0
        break
    return ans

  def maxOperations(self, nums: List[int], k: int) -> int:
    nums = sorted(nums)
    ans = 0
    l = 0
    r = len(nums) - 1
    while l < r:
      if nums[l] + nums[r] < k:
        l += 1
      elif nums[l] + nums[r] > k:
        r -= 1
      else:
        ans += 1
        l += 1
        r -= 1

    return ans


if __name__ == "__main__":
  # s = Solution().maxOperations([1, 2, 3, 4], 5)
  s = Solution().maxOperations([3, 1, 3, 4, 3], 6)
  print(s)
