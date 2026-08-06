class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        chars1 = {}
        chars2 = {}

        for i in range(len(s)):
            chars1[s[i]] = chars1.get(s[i], 0) + 1;
            chars2[t[i]] = chars2.get(t[i], 0) + 1;

        return chars1 == chars2;
