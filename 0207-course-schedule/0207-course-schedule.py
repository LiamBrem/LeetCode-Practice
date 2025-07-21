from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)

        for course, p in prerequisites:
            courseMap[course].append(p)

        taken = set()

        def dfs(course):
            if not courseMap[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in courseMap[course]:
                if not dfs(p):
                    return False

            courseMap[course] = []
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True