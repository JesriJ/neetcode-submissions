class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums)+1)]
        cnt = {}

        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        
        for n in cnt:
            freq[cnt[n]].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
        
