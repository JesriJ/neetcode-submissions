class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        start, end = 0, 0

        while end < len(s):
            while end < len(s) and s[end] != "#":
                end += 1
            l = int(s[start:end])
            start = end + 1
            end = start + l
            res.append(s[start:end])
            start = end
        
        return res
            
