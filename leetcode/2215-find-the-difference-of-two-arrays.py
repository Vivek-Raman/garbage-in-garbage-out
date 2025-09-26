from typing import List


class Solution:
  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    notIn1 = set(nums2) - set(nums1)
    notIn2 = set(nums1) - set(nums2)
    return [list(notIn2), list(notIn1)]


if __name__ == "__main__":
  print(Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
