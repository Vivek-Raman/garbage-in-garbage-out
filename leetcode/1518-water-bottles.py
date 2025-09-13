class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed = (numBottles // numExchange) * numExchange
        carry = (numBottles // numExchange) + (numBottles % numExchange)
        if carry >= numExchange:
            return consumed + self.numWaterBottles(carry, numExchange)
        return consumed + carry


if __name__ == '__main__':
    print(Solution().numWaterBottles(9, 3))
