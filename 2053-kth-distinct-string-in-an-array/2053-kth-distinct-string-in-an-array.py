from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distribution = dict()
        for s in arr:
            if s in distribution:
                distribution[s] += 1
            else:
                distribution[s] = 1

        for value, frequency in distribution.items():
            if frequency == 1:
                if k > 1:
                    k -= 1
                else:
                    return value
        return ''


if __name__ == '__main__':
    print(Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
