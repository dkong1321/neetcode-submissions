class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        result = []
        
        print(hashmap)

        visited, cycle = set(), set()

        def dfs(course):
            # Catches cycles within the loop
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            # go through the prereqs
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            # Need to remove the course for this run if we finished 
            # going down a path
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result 