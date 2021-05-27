# Graph

+ [Is Graph Bipartite?](#is-graph-bipartite)

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

``` python
def isBipartite(self, graph: List[List[int]]) -> bool:
    n = len(graph)
    color = {}
    def dfs(u):
        for v in graph[u]:
            if v not in color:
                color[v] = 1 - color[u]
                if not dfs(v): return False
            elif color[v] == color[u]:
                return False
        return True
    for i in range(n):
        if i not in color and graph[i]:
            color[i] = 1
            if not dfs(i): return False
    return True
```

