from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num1 in nums1:
            try:
                nums2.remove(num1)
                intersection += [num1]
            except ValueError:
                continue
        return intersection


if __name__ == '__main__':
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))
