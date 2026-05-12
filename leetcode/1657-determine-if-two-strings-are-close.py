# 1657. Determine if Two Strings Are Close

from collections import Counter


class Solution:

  def closeStrings(self, word1: str, word2: str) -> bool:
    freq1 = Counter(word1)
    freq2 = Counter(word2)
    letters1 = freq1.keys()
    letters2 = freq2.keys()
    if letters1 != letters2:
      return False

    counts1 = list(freq1.values())
    counts1.sort()
    counts2 = list(freq2.values())
    counts2.sort()

    return counts1 == counts2


if __name__ == "__main__":
  s = Solution().closeStrings("abbzzca", "babzzcz")
  print(s)
