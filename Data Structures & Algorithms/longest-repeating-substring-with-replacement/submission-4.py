class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # # Brute Force
        res = 0

        for i in range(len(s)):
            count, max_freq = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                max_freq = max(max_freq, count[s[j]])
                if (j-i+1) - max_freq <= k:
                    res = max(res, j-i+1)
        return res

        # Optimal

        count = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r-l+1) - max_freq > k:
                count[s[r]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
        