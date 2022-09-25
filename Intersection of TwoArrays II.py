class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         res = []
        
#         map1 = defaultdict(int)
#         map2 = defaultdict(int)
        
#         for i in range(len(nums1)):
#             if nums1[i] not in map1:
#                 map1[nums1[i]] = 1
#             else:
#                 map1[nums1[i]] += 1
                
#         for i in range(len(nums2)):
#             if nums2[i] not in map2:
#                 map2[nums2[i]] = 1
#             else:
#                  map2[nums2[i]] += 1
                
#         for n in map1:
#             if n in map2:
#                 res.extend(min(map1[n], map2[n])*[n])
                
#         return res
    
#     Simplified:
        map1 = collections.Counter(nums1)
        map2 = collections.Counter(nums2)
        
        res = []
        
        for key in map1.keys() & map2.keys():
            res.extend([key]*min(map1[key], map2[key]))
            
        return res
            