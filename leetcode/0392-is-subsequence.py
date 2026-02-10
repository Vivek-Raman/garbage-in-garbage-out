class Solution:

  def isSubsequence(self, s: str, t: str) -> bool:
    len_s = len(s)
    if len_s == 0:
      return True
    len_t = len(t)
    if len_t == 0:
      return s == 0

    l = 0
    while l < len_t:
      if t[l] != s[0]:
        l += 1
        continue
      i = 0
      while i < len_s and l + i < len_t:
        if s[i] == t[l + i]:
          # print(f'Found "{s[i]}" ({i}) at {l + i}')
          i += 1
        else:
          l += 1

      if i == len_s:
        return True
      else:
        l += 1
    return False


if __name__ == '__main__':
  print(Solution().isSubsequence('bcd', 'uuuubcd'))
