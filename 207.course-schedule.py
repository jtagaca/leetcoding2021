#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Solution:
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacent list
        # # perform dfs
        # check if there is a cycle
        # we bubble or just stop after base conditions

        hashm = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            hashm[course].append(prereq)
        visitedStack = set()
        # check if I still have access to hashmap

        def dfs(hashm, visitedStack, course):
            nonlocal Visited
            # if we have a cycle
            if course in visitedStack:
                return False

            Visited.add(course)

            # if we have an empyt
            if hashm[course] == []:
                return True

            visitedStack.add(course)
            for prereq in hashm[course]:
                isPossible = dfs(hashm, visitedStack, prereq)

            visitedStack.remove(course)

            return True and isPossible

        Visited = set()
        for i in range(numCourses):
            if i in Visited:
                continue
            output = dfs(hashm, visitedStack, i)
            if output == False:
                return False
        return True
# @lc code=end

