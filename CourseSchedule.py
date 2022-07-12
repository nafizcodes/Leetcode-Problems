class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
    #visitSet to store the visited courses
        visitSet = set()
        
        def dfs(crs):
            #if the course is in visitSet then meaning creating a loop, so return False
            if crs in visitSet:  
                return False
            #if the course has no preq then return true
            if preMap[crs] == []:
                return True
            #if both the conditions are False, then add the course to visitset
            visitSet.add(crs)
            for i in preMap[crs]:
                if not dfs(i):  # a course cannot be taken
                    return False
                
            visitSet.remove(crs)
            
            preMap[crs] = []    #to mark the course preq as empty
            return True
            
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
    
    
#Time Complexity - O(n+p)
#Space complexity - O(n+p)