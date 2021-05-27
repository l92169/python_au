# Intervals

+ [Number of Islands](#number-of-islands)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

``` python
def numIslands(self, grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                self.dfs(grid, i, j)
    return count


def dfs(self, grid, r, c):
    grid[r][c] = "0"
    arr = [(-1,0), (1,0), (0,-1), (0,1)]
    for r_1, c_1 in arr:
        r_2 = r + r_1
        c_2 = c + c_1
        if 0 <= r_2 < len(grid) and 0 <= c_2 < len(grid[0]) and grid[r_2][c_2] == "1":
            self.dfs(grid, r_2, c_2)
```
