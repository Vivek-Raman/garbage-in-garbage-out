import math
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5]
        if n == 1:
            return 1
        elif n < 4:
            return factors[n - 2]

        uglies = factors[:]
        uglies.insert(0, 1)
        uglies_set = set(uglies)
        heapq.heapify(uglies)

        base_index = 0
        nth_ugly = 1
        for _ in range(n):
            nth_ugly = heapq.heappop(uglies)
            for factor in factors:
                ugly = nth_ugly * factor
                if ugly not in uglies_set:
                    uglies_set.add(ugly)
                    heapq.heappush(uglies, ugly)
            base_index += 1
        return nth_ugly


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
