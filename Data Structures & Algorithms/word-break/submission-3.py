class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):

            for w in wordDict:
                if(len(w)+i <= len(s) and w == s[i:len(w)+i]):
                    dp[i] = dp[len(w)+i]
                if dp[i]:
                    break
        
        return dp[0]