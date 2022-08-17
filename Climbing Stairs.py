class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 1
        
        for i in range(n-1):
            temp = one   # to store the 'one' value and use it to initialize 'two' variable
            one = two + one
            two = temp
            
        return one
    
    
#        n = 5
# levels     0   1   2   3   4   5
#  ways      8   5   3   2   1   1
#                           one  two 
                      
            