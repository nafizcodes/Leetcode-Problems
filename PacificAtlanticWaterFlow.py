class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights) , len(heights[0])
        
        pac , atl = set() , set()  #set to mark which cells can reach pacific and atlantic respectively
        res = []
        
        def dfs(r, c, visited, prevHeight):
            if ((r,c) in visited or r < 0 or r == ROWS  #careful of the visited edge case
                or c < 0 or c == COLS or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        
        for c in range(COLS): #EVERY COL
            dfs(0, c, pac, heights[0][c])    #first row   #prevHeight to check if prev is less
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])  #last row
            
            
        for r in range(ROWS): #EVERY ROW
            dfs(r, 0, pac, heights[r][0])  #first column
            dfs(r, COLS-1, atl, heights[r][COLS-1])    #last column
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
                    
        return res
            
#Reference : https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1126937/Pacific-Atlantic-Water-Flow-or-Short-and-Easy-w-Explanation-and-diagrams
            
    
        
