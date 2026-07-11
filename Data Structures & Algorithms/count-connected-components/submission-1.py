class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}
        visit = [False for i in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res