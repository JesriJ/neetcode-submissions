class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        mp = {}
        res = 0

        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            res = max(res, (r-l)+1)
            mp[s[r]] = r
            r += 1
        
        return res
