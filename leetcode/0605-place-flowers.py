from typing import List


class Solution:

  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
      curr_blank = flowerbed[i] == 0
      if curr_blank:
        prev_blank = i == 0 or flowerbed[i - 1] == 0
        next_blank = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

        if next_blank and prev_blank and n > 0:
          n -= 1
          flowerbed[i] = 1

    return n == 0


if __name__ == "__main__":
  s = Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1)
  print(s)
