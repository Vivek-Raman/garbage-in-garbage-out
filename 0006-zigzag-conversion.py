class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [[] for i in range(numRows)]
    # interval = 2 * (numRows - 2) + 1
    fwd = False # flipped immediately on 1st loop iteration
    zig = 0
    for i in range(0, len(s)):
      rows[zig].append(s[i])
      if zig == numRows - 1 or zig == 0:
        fwd = not fwd

      zig += 1 if fwd else -1
    # print(rows)
    return ''.join([''.join(rows[i]) for i in range(len(rows))])


if __name__ == '__main__':
  print(Solution().convert("PAYPALISHIRING", 3))
