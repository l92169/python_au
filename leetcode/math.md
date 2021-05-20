# Math

+ [K Closest Points to Origin](#k-closest-points-to-origin)

## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

``` python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda x: pow((x[0]**2 + x[1]**2), 0.5))
    return points[:k]
```

