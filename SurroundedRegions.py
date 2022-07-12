    # BFS
    def solve(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "."
                queue.extend([(r-1, c),(r+1, c),(r, c-1),(r, c+1)])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"

#DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r,c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            
            capture(r, c+1)
            capture(r, c-1)
            capture(r+1, c)
            capture(r-1, c)
            
            
        #1. DFS - Capture unsurrounding regions (O -> T)
        
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1])):
                    capture(r,c)
                    
        #2  DFS - Capture surrounding regions (O -> X)
        
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == 'O'):
                    board[r][c] = 'X'
                elif(board[r][c] == 'T'):
                    board[r][c] = 'O'
                    
                    
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if(board[r][c] == 'T'):
        #             board[r][c] = 'O'
            
        