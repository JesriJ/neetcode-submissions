class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Key: char count, Val: str
        res = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord('a')-ord(c)] += 1
            res[tuple(char_count)].append(s)
        
        return list(res.values())

