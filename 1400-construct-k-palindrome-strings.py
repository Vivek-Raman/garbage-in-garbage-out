class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    if len(s) == k:
      return True
    if (len(s) < k):
      return False

    char_counts = dict()
    for c in s:
      if (c not in char_counts):
        char_counts[c] = 0
      char_counts[c] += 1
    # print(char_counts)

    freq_counts = dict()
    freq_counts[0] = 0
    freq_counts[1] = 0
    for char, count in char_counts.items():
      freq_counts[count % 2] += 1
    # print(freq_counts)

    return freq_counts[1] <= k


if __name__ == '__main__':
  print(Solution().canConstruct("annabelle", 2))
