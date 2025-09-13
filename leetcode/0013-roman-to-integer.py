class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        for i in range(len(s)):
            letter = s[i]
            value = value_map[letter]
            if i < len(s) - 1 and value_map[s[i + 1]] > value:
                sum -= value
            else:
                sum += value

        return sum


if __name__ == '__main__':
    print(Solution().romanToInt('IL'))
