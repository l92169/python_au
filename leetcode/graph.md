# Graph

+ [Course Schedule II](#course-schedule-ii)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

``` python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    arr = []
    todo = {i: set() for i in range(numCourses)}
    outdegree = [[] for _ in range(numCourses)]
    for i in prerequisites:
        todo[i[0]].add(i[1])
        outdegree[i[1]].append(i[0])
    start = [i for i in range(numCourses) if not todo[i]]
    while start:
        newStart = []
        for i in start:
            arr.append(i)
            for j in outdegree[i]:
                todo[j].remove(i)
                if not todo[j]:
                    newStart.append(j)
        start = newStart
    return arr if len(arr) == numCourses else []

```

