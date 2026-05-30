class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        start = 0
        end = 0

        # while i < len(s):
        #     if s[i] == "#":
        #         length = int(s[prev:i])
        #         res.append(s[i+1 : i+1+length])
        #         prev = i + 1 + length
        #         i = prev
        #         continue
        #     i += 1
        while end < len(s):
            if s[end] == "#":
                length = int(s[start:end])
                start = end + 1
                end = end + 1 + length
                res.append(s[start : end])
                start = end
                continue
            end += 1
        
        return res
            
                    
            

  