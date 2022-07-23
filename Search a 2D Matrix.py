class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix), len(matrix[0]) #dimensions of matrix
        
        top , bot = 0, ROWS - 1
        
        #matrix will never be empty by condition
        
        while top <= bot:  
            midrow = (top + bot)//2
            
            if target > matrix[midrow][-1] :
                top = midrow + 1
            elif target < matrix[midrow][0] :
                bot = midrow - 1
            else : #here the target is within the midrow 
                break  
                
        # if we did not break, it would mean top <= bot invalid as it would mean that none of the rows 
        
        if not (top <= bot):  #means target is not found in any of the rows and top pointer is no longer smaller than bottom
            return False
        
        midrow = (top + bot) //2
        
        l, r = 0 , COLS - 1
        
        while l <= r:
            m = (l+r) // 2
            
            if target > matrix[midrow][m]:
                l = m + 1
            
            elif target <  matrix[midrow][m]:
                r = m - 1
                
            else:
                return True
            
        return False
            