# Math

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

``` python
def largestPerimeter(self, A: List[int]) -> int:
    maxx=0
    for i in range(0,len(A) - 2):
        for j in range(i+1,len(A) - 1):
            for t in range(j + 1,len(A)):
                if A[i] + A[j] > A[t] and A[i] + A[t] > A[j] and A[t] + A[j] > A[i]:
                    if A[i] + A[j] + A[t] > maxx:
                        maxx = A[i] + A[j] + A[t]
    return maxx
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

``` python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort()
    A = list(reversed(A))
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2] 
    return 0
```
