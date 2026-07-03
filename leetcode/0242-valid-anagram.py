# 242. Valid Anagram


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = Counter(s)
        hash_t = Counter(t)
        return hash_s == hash_t


pass


if __name__ == "__main__":
    s = Solution().isAnagram(s="anagram", t="nagaram")
    print(s)
