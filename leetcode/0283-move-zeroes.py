from typing import List


class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    last_ne_zero_idx = 0
    while i < len(nums):
      if nums[i] != 0:
        temp = nums[last_ne_zero_idx]
        nums[last_ne_zero_idx] = nums[i]
        nums[i] = temp
        last_ne_zero_idx += 1
      i += 1


if __name__ == '__main__':
  nums = [0,1,0,3,12]
  s = Solution().moveZeroes(nums)
  print(nums)
  nums = [0,0,1]
  s = Solution().moveZeroes(nums)
  print(nums)
