from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        for each cell if it has neighbors that are higher than it we should stop looking
        if the cell is at the end of both the top and left and thr bot right it has hit both oceans
        collect the coords that touch the pacific (heights[0], heights[range(len(heights)][0])])
        altnatic (heights[len(heights)], and heights[0][range(len(heights)])])
        """
        directions = [[1,0], [0,1], [-1,0],[0,-1]]
        rows, cols = len(heights), len(heights[0])
        res = []
        visited = set()
       
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit 
                or r == len(heights) or c == len(heights[0]) 
                or r < 0 or c < 0 
                or heights[r][c] < prevHeight):
                    return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr,c+dc,visit,heights[r][c])

        # get all the cells for the first row (pacific)
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0])-1, atl, heights[r][cols -1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
