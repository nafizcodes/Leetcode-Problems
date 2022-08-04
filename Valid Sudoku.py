class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)    # each col : {}
        rows = collections.defaultdict(set)    # each row : {}
        squares = collections.defaultdict(set)  # (row,col) : {}
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':  # ignore the empty boxes, only care about the filled ones
                    continue
                
                if (board[r][c] in rows[r] or  # check if there is any duplicate in a row
                    board[r][c] in cols[c] or  # check if there is any duplicate in a row                   0 1 2
                    board[r][c] in squares[(r//3, c//3)]):  #check if the square has any duplicate        0
                                                #r//3, c//3 -- floor division divides the board into 3    1
                    return False                                            #                             2
                
                # add the values to each set if not already in the sets
                rows[r].add(board[r][c])      
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])   # {(0,0) : {}, (0,1): {}, (0,2): {}.....}
                
        return True
                