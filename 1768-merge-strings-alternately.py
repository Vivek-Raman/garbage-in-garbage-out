class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    res = ''
    idx1 = 0
    idx2 = 0
    while idx1 < len(word1) and idx2 < len(word2):
      res += word1[idx1]
      res += word2[idx2]
      idx1 += 1
      idx2 += 1
    while idx1 < len(word1):
      res += word1[idx1]
      idx1 += 1
    while idx2 < len(word2):
      res += word2[idx2]
      idx2 += 1
    return res


if __name__ == '__main__':
  print(Solution().mergeAlternately(word1 = "abc", word2 = "pqr"))
  print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))
