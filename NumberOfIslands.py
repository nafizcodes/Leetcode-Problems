class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1': #HANDLE EDGE CASES
            return                #RETURN NOTHING AS NO ISLAND

        grid[i][j] = '#' #   #'#' can be anything -  modifies the input to ensure that the count isn't incremented where we could accidentally traverse the same '1' cell multiple times and get into an infinite loop within an island
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


