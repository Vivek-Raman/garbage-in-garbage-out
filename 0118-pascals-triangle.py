from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for row_number in range(numRows):
            row = []
            for cell_number in range(row_number + 1):
                val = 1
                if 1 <= cell_number < row_number and row_number > 1:
                    up_left = tri[row_number - 1][cell_number]
                    up_right = tri[row_number - 1][cell_number - 1]
                    val = up_left + up_right
                row.append(val)
            tri.append(row)
        return tri


if __name__ == '__main__':
    print(Solution().generate(5))
