from typing import List


class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans = [1 for n in nums]
    c = 1
    for i in range(len(nums)):
      ans[i] *= c
      c *= nums[i]
    c = 1

    for i in range(len(nums) - 1, -1, -1):
      ans[i] *= c
      c *= nums[i]
    return ans


if __name__ == "__main__":
  s = Solution().productExceptSelf([1, 2, 3, 4])
  print(s)
