from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        directions = [(1,0), (0,1), (-1,0),(0,-1)]
        
        # This will give us each row
        for i in  range(len(grid)):
            # This will go through each column in a row
            for j in range(len(grid[0])):
                # If we have an island we need to increase the count 
                # and a value to the set()
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    visited.add((i,j))
                    # instantiate the queue with the new island
                    queue = deque([(i,j)])
                    while queue:
                        i, j = queue.popleft()
                        # run logic to find its neighbors they cannot be counted as an island
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if (ni >= 0 and ni < len(grid) 
                            and nj >= 0 and nj < len(grid[0]) 
                            and grid[ni][nj] == "1"
                            and (ni,nj) not in visited):
                                visited.add((ni,nj))
                                queue.append((ni,nj))
                            

        return islands