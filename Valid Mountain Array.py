class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        i = 0
        
        while i < len(arr) and i+1 < len(arr) and arr[i+1] > arr[i]:
                i += 1
                
        if i == 0 or i+1 >= len(arr):
            return False
        
        while i < len(arr) and i+1 < len(arr):
            if arr[i+1] >= arr[i]:
                return False
            i += 1
        return True
            
            