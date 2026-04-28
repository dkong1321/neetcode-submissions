from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    queue = deque([(r,c)])
                    island += 1
                    visited.add((r,c))
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = row +dr, col+dc
                            if (nr >= 0 and nr < len(grid) and nc >= 0 
                                and nc < len(grid[0]) 
                                and (nr, nc) not in visited 
                                and grid[nr][nc] == "1"):
                                visited.add((nr,nc))
                                queue.append((nr,nc))
        return island