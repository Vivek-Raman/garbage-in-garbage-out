from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        for index, char in enumerate(strs[0]):
            for st in strs:
                if index >= len(st) or st[index] != char:
                    return lcp
            lcp += char
        return lcp


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["ab","a"]))
