class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        i, j = 0, 0
        res = []

        while j < len(s):
            i = j
            while s[i] != "#":
                i += 1
            l = int(s[j:i])
            i = i + 1
            j = i + l
            res.append(s[i:j])

        return res
        