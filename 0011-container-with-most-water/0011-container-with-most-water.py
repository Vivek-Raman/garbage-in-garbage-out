from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
    length = len(height)
    i = 0
    j = length - 1
    max_area = -1
    while i < length and j >= 0:
      area = min(height[i], height[j]) * (j - i)
      if area > max_area:
        max_area = area
      if height[i] < height[j]:
        i += 1
      else:
        j -= 1

    return max_area


if __name__ == '__main__':
  print(Solution().maxArea([8,7,2,1]))
