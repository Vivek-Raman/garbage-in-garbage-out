class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(n)]
        current_index = 0
        while len(players) > 1:
            current_index = (current_index + (k - 1)) % len(players)
            players.pop(current_index)
        return players[0] + 1


if __name__ == '__main__':
    print(Solution().findTheWinner(6, 5))
