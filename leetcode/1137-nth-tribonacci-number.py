# 1137. N-th Tribonacci Number


class Solution:

  def __init__(self):
    self.cache = [-1] * 40

  def tribonacci(self, n: int) -> int:
    if self.cache[n] >= 0:
      return self.cache[n]
    if n <= 0:
      return 0
    if n <= 2:
      return 1
    result = self.tribonacci(n - 3) + self.tribonacci(
        n - 2) + self.tribonacci(n - 1)
    self.cache[n] = result
    return result


if __name__ == "__main__":
  s = Solution().tribonacci(31)
  print(s)
