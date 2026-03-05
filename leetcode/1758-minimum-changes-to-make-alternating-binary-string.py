class Solution:

  def minOperations_fail(self, s: str) -> int:
    op_count = 0
    prev = s[0]

    for i in range(1, len(s)):
      print(f'{i}, {prev}{s[i]}')
      if s[i] == prev:
        # match --> flip current
        print(f'prev {prev}, seen {s[i]}, flip {op_count+1}')
        prev = '1' if s[i] == '0' else '0' if s[i] == '1' else '-'
        op_count += 1
      else:
        prev = s[i]

    return op_count

  def flip(self, c: str) -> str:
    return '1' if c == '0' else '0'

  def minOperations(self, s: str) -> int:
    l = len(s)
    ops_if_start_with_0 = 0
    ops_if_start_with_1 = 0
    target_if_start_with_0 = '0'
    target_if_start_with_1 = '1'
    for i in range(l):
      target_if_start_with_0 = self.flip(target_if_start_with_0)
      target_if_start_with_1 = self.flip(target_if_start_with_1)
      c = s[i]
      if s[i] != target_if_start_with_0:
        ops_if_start_with_0 += 1
      if s[i] != target_if_start_with_1:
        ops_if_start_with_1 += 1
    return min(ops_if_start_with_0, ops_if_start_with_1)


if __name__ == "__main__":
  # s = Solution().minOperations('0100')
  s = Solution().minOperations("10010100")
  print(s)
