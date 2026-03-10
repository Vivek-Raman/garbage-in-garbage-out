from typing import List


class Solution:

  def longestCommonPrefix_bruteForce(self, strs: List[str]) -> str:
    lcp = ''
    for index, char in enumerate(strs[0]):
      for st in strs:
        if index >= len(st) or st[index] != char:
          return lcp
      lcp += char
    return lcp

  def longestCommonPrefix(self, strs: List[str]) -> str:
    strs = sorted(strs)
    l = strs[0]
    r = strs[-1]
    lcp = ''
    for i in range(min(len(l), len(r))):
      if l[i] == r[i]:
        lcp += l[i]
      else:
        break
    return lcp


if __name__ == '__main__':
  print(Solution().longestCommonPrefix(["cluster", "clue", "clumsy"]))
