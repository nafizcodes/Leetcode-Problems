class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        area = 0
        def dfs(grid, i, j):

            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0: #HANDLE EDGE CASES or can be written not                                                                                   grid[i][j] for last condition
                return 0               #RETURN 0 as area

            grid[i][j] = 0   #checks off the visited cell as 0 and adding the value of this cell which is 1 in the return statement where we are adding 1 to the result
            
            return (1 + dfs(grid, i+1, j) +
            dfs(grid, i-1, j)+
            dfs(grid, i, j+1)+
            dfs(grid, i, j-1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(grid, i, j))
        return area

