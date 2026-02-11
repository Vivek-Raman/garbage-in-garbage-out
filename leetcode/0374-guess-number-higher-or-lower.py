# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

ans = 6


def guess(num: int) -> int:
  if num == ans:
    return 0
  diff = ans - num
  return diff // abs(diff)


class Solution:

  def doGuess(self, n: int, l: int, r: int):
    mid = (l + r) // 2
    v = guess(mid)
    if v == 0:
      return mid
    elif v < 0:
      return self.doGuess(n, l, mid)
    elif v > 0:
      return self.doGuess(n, mid, r)

  def guessNumber(self, n: int) -> int:
    return self.doGuess(n, 1, n)


if __name__ == "__main__":
  s = Solution().guessNumber(10)
  print(s)
