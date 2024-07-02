from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        for index1, num1 in enumerate(nums):
            index2 = number_map.get(target - num1, -1)
            number_map[num1] = index1
            if index2 >= 0 and index1 != index2:
                return [index1, index2]


if __name__ == '__main__':
    print(Solution().twoSum([3,3], 6))
