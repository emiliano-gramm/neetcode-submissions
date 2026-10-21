from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        path = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i in range(len(prerequisites)):
            path[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        if not q:
            return False

        while q:
            course = q.pop()
            for c in path[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return sum(indegree) == 0