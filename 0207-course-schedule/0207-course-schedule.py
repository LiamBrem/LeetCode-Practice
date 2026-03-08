"""
0: 1, 2, 4
1: 2, 4
2: 3
3: 4

0: 
1: 0
2: 0, 1
3: 2
4: 0, 1, 3

"""

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list) # {course -> prereq}
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        seen = set()

        def dfs(course):
            if not courseMap[course]:
                return True

            if course in seen:
                return False

            seen.add(course)

            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False

            courseMap[course] = []
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        
        

        
        