class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        start, end = 0, 0
        res = []

        while end < len(s):
            start = end
            while s[start] != "#":
                start += 1
            l = int(s[end:start])
            start = start + 1
            end = start + l
            res.append(s[start:end])

        return res
        