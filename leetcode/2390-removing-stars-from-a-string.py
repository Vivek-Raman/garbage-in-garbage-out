class Solution:
  def removeStars(self, s: str) -> str:
    a = []
    for c in s:
      if c == '*':
        a.pop()
      else:
        a.append(c)
    return ''.join(a)


if __name__ == '__main__':
  s = Solution().removeStars('leet**cod*e')
  print(s)
