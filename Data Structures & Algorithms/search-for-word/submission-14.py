class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r, c, w):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visit):
                return False
            
            visit.add((r,c))
            w += board[r][c]
            if word == w:
                return True
            
            res = (dfs(r+1, c, w) or
            dfs(r-1, c, w) or
            dfs(r, c+1, w) or
            dfs(r, c-1, w))
            visit.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, ""):
                    return True
        
        return False