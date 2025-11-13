class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left, max_longest = 0, 0
        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            max_longest = max(max_longest, right - left + 1)
        return max_longest

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
