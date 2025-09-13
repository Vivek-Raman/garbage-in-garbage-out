class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique_chars = set()
        length = len(s)
        left = 0
        for right in range(length):
            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                while s[right] in unique_chars:
                    unique_chars.remove(s[left])
                    left += 1
                unique_chars.add(s[right])
        return longest

    def lengthOfLongestSubstring_BAD(self, s: str) -> int:

        longest_substring = 0
        for start_index, start in enumerate(s):
            substring = set()
            remaining = s[start_index:]
            for index, c in enumerate(remaining):
                if index >= len(remaining) - 1:
                    substring.add(c)
                    longest_substring = max(len(substring), longest_substring)
                    break
                if c in substring:
                    longest_substring = max(len(substring), longest_substring)
                    break
                substring.add(c)
        return longest_substring


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcpr'))
