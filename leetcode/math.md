#Math

##Largest Perimeter Triangle

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

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