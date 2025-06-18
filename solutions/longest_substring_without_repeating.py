# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=rabvlt31

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r, char in enumerate(s):
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            res = max(res, r-l + 1)
        
        return res