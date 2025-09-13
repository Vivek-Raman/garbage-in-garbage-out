from typing import List


class Solution:
  def compress(self, chars: List[str]) -> int:
    original_length = len(chars)

    if original_length == 1:
      return 1

    read_idx = 0
    l = 0
    while read_idx < original_length:
      group_length = 1

      while read_idx + group_length < original_length and chars[read_idx + group_length] == chars[read_idx]:
        group_length += 1
      chars[l] = chars[read_idx]
      l += 1

      if group_length > 1:
        num_str = str(group_length)
        chars[l:l + len(num_str)] = list(num_str)
        l += len(num_str)
      read_idx += group_length

    print(''.join(chars), chars)
    return l

if __name__ == '__main__':
  print(Solution().compress(chars = ["a","a","a","b","b","a","a"]))
  # print(Solution().compress(chars = ["a","a","b","b","c","c","c"]))
  # print(Solution().compress(chars = ["a"]))
