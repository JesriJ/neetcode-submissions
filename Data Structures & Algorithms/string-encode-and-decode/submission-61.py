class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        prev = 0
        i = 0

        # while i < len(s):
        #     if s[i] == "#":
        #         length = int(s[prev:i])
        #         res.append(s[i+1 : i+1+length])
        #         prev = i + 1 + length
        #         i = prev
        #         continue
        #     i += 1
        while i < len(s):
            if s[i] == "#":
                length = int(s[prev:i])
                prev = i+1
                i = i + 1 + length
                res.append(s[prev : i])
                prev = i
                continue
            i += 1
        
        return res
            
                    
            

  