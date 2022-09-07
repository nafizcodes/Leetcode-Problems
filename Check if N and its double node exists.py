class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        unique = set()
        
        for i in range(len(arr)):
            
            if (arr[i]*2 in unique) or (arr[i]/2 in unique and arr[i] % 2 == 0):
                return True
            
            unique.add(arr[i])
            

        return False
    