class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time + 1
        turns = (time // (n - 1))
        delta = (time % (n - 1))

        if turns % 2 == 1:
            return n - delta
        return delta + 1


if __name__ == '__main__':
    # print(Solution().passThePillow(5, 4))
    print(Solution().passThePillow(18, 38))
