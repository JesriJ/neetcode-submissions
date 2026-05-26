class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False

        # s_map = {}
        # t_map = {}

        # for i in range(len(s)):
        #     s_map[s[i]] = 1 + s_map.get(s[i], 0)
        #     t_map[t[i]] = 1 + t_map.get(t[i], 0)

        # return s_map == t_map

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord('a')-ord(s[i])] += 1
            count[ord('a')-ord(t[i])] -= 1
        
        for n in count:
            if n != 0:
                return False
        
        return True