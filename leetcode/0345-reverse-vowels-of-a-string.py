class Solution:
  def reverseVowels(self, s: str) -> str:
    s_list = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    f = 0
    r = len(s_list) - 1
    while f <= r:
      while f <= r and s_list[f] not in vowels:
        f += 1
      while f <= r and s_list[r] not in vowels:
        r -= 1
      if f >= r:
        break
      temp = s_list[r]
      s_list[r] = s_list[f]
      s_list[f] = temp
      f += 1
      r -= 1
    return ''.join(s_list)


if __name__ == "__main__":
  s = Solution().reverseVowels(",.")
  print(s)
