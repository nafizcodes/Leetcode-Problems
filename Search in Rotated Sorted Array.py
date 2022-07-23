class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0,len(nums)- 1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            
             # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] 
            if A[left] <= target < A[mid] 
            else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] 
            if A[mid] < target <= A[right] 
            else, search left side
            """

            #left rotated 
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            #right rotated
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
    
    # 0 1 2 4 5 6 7
    
    # 4 5 6 7 0 1 2
            