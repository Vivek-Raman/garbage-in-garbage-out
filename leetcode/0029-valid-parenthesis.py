class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        start_chars = ('[', '{', '(')
        stack = []
        for char in s:
            if char in start_chars:
                stack += [char]
            else:
                mapped = bracket_map.get(char)
                if len(stack) <= 0 or mapped is not stack[-1]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid(']'))
