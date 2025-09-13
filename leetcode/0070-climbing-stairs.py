class Solution:
  def climbStairs(self, n: int) -> int:
    cache = {}
    cache[1] = 1
    cache[2] = 2
    def fib(n: int) -> int:
      if n in cache:
        return cache[n]
      val = fib(n - 1) + fib(n - 2)
      cache[n] = val
      return val
    return fib(n)


if __name__ == '__main__':
  print(Solution().climbStairs(5))
