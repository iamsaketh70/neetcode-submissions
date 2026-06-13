class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={i:[] for i in range(numCourses)}
        visited=set()
        done=set()
        res=[]
        for course,pre in prerequisites:
            courses[course].append(pre)
        def dfs(course):
            if course in visited:
                return False
            if course in done:
                return True

            visited.add(course)
            
            for pre in courses[course]:
                if not dfs(pre):return False
            
            visited.remove(course)
            courses[course]=[]
            done.add(course)
            res.append(course)
            
            return True

        for pre in range(numCourses):
            if not dfs(pre):return []
        
        return res
            



        