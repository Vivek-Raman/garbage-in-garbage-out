# 88. Merge Sorted Array

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        r = 0
        res = [-1] * (m + n)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res[r] = nums1[i]
                i += 1
            else:
                res[r] = nums2[j]
                j += 1
            r += 1
        while i < m:
            res[r] = nums1[i]
            r += 1
            i += 1
        while j < n:
            res[r] = nums2[j]
            r += 1
            j += 1
        nums1[:] = res


pass


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    s = Solution().merge(nums1, m=3, nums2=[2, 5, 6], n=3)
    print(nums1)
