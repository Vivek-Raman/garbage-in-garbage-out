class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = str(x)
        for i in range(len(number) // 2):
            if number[i] != number[len(number) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(122))
