class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Brute Force
        max_len = 0
        
        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                chars.add(s[j])
            max_len = max(max_len, len(chars))
        
        return max_len


        # Optimal
        # mp = {}
        # l = 0
        # max_len = 0

        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l = max(mp[s[r]] + 1, l)
        #     mp[s[r]] = r
        #     max_len = max(max_len, r-l + 1)
        # return max_len
                

        
            