class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses={}
        courses={i:[] for i in range(numCourses)}
        visited=set()
        for pre,course in prerequisites:
            courses[course].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if course ==[]:
                return True
            visited.add(course)
            for pre in courses[course]:
                if not dfs(pre):return False
            visited.remove(course)
            courses[course]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True