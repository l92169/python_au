# Arrays

## Transpose Matrix

+ [Transpose Matrix](#transpose-matrix)

https://leetcode.com/problems/transpose-matrix/

``` python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    new_arr = [[0]*len(A) for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            new_arr[i][j] = A[j][i]
    return new_arr
```