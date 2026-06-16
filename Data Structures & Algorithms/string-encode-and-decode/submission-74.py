class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res



    def decode(self, s: str) -> List[str]:

        start = 0
        end = 0
        res = []

        while end < len(s):
            if s[end] == "#":
                l = int(s[start:end])
                start = end + 1
                end = start + l
                res.append(s[start:end])
                start = end
                end += 1
            else:
                end += 1
        
        return res


