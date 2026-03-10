# 1456. Maximum Number of Vowels in a Substring of Given Length


class Solution:

  def maxVowels(self, s: str, k: int) -> int:
    VOWELS = 'aeiou'

    l = 0
    r = 0
    run_vowels = 0
    while r < k:
      if s[r] in VOWELS:
        run_vowels += 1
      r += 1
    max_vowels = run_vowels

    while r < len(s):
      if s[l] in VOWELS:
        run_vowels -= 1
      if s[r] in VOWELS:
        run_vowels += 1
      max_vowels = max(run_vowels, max_vowels)
      l += 1
      r += 1

    return max_vowels


if __name__ == "__main__":
  s = Solution().maxVowels(s="leetcode", k=3)
  print(s)
