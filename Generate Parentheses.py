class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()   # after the backtrack returns we pop the whole sequence because we have only one stack variable to keep track of the sequences
                
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        
        return res