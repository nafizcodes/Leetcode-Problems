class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(nums, left, right, target):

            if right>=left:
                halfIndex = floor((left+right)/2)

                if nums[halfIndex] == target:
                    return halfIndex
                elif nums[halfIndex] > target:
                    right = halfIndex - 1
                    return binarySearch(nums, left, right, target)
                elif nums[halfIndex] < target:
                    left = halfIndex + 1
                    return binarySearch(nums, left, right, target)
            else:
                return -1
        
        return binarySearch(nums, 0, len(nums) -1, target)
    
    
    
#Iterative solution - >>>
# class Solution:
#     def search(self,nums:List[int],target:int)->int:
#         1,r=0,len(nums)-1
#         while1<=r:
#             m=(1+r)//2
#             if nums[m]>target:
#                 r=m-1
#             elif nums[m]<target:
#                 1=m+1
#             else:
#                 returnm
#         return -1