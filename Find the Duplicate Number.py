class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Pigeon hole Principle - If there are n+1 numbers and the range is 1:n
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        pointer = nums[0]
        
        while slow != pointer:
            slow = nums[slow]
            pointer = nums[pointer]
            
        
        return slow
            
        # Time - O(n)   Space - O(1)
        
        
        
  # Solution:  Sort()  T - O(nlogn) - Sorting takes O(nlogn) + O(n) to iterate so worst case  O(nlogn)    
# Space - O(n) 
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return nums[i]            

# Set Solution  T-O(n)  S - O(n)
 # class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)
