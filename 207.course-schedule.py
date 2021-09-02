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
            # if we have a cycle we use this
            if course in visitedStack:
                return False

            # if we have an empyty neighbor it means we do not need to traverse
            if hashm[course] == []:
                return True

            # we keep track of cycles using this
            visitedStack.add(course)
            for prereq in hashm[course]:
                isPossible = dfs(hashm, visitedStack, prereq)
                # if we ever see false then we know we just stop that call and return false all the way
                if isPossible == False:
                    return False
            # once we finish the call we have to remove it and mark it empty since we saw that
            # there was no cycle and we can now be sure that we do not have to visit it twice
            visitedStack.remove(course)
            hashm[course] = []

            return True

        # dealing with disjoin graphs
        # we have a root where everything is accessable and we traverse
        # normally we have a tracker of visited to not visit node twice
        for i in range(numCourses):
            output = dfs(hashm, visitedStack, i)
            if output == False:
                return False
        return True
