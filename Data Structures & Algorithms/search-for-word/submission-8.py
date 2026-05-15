class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (0, 1), (-1,0),(0,-1)]
        row = len(board)
        col = len(board[0])
        path = set()

        def dfs(r, c, i):
            # passing condition
            if i == len(word):
                return True

            # fail condition
            if (r < 0 or r >=row or c < 0 or 
                c >=col or board[r][c] != word[i] or (r,c) in path):
                return False
            
            path.add((r,c))
            for dr, dc in directions:
                if dfs(r+dr, c+dc, i+1):
                    return True
            path.remove((r,c))

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        
        return False