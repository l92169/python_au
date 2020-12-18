# Array

## Flipping an Image

+ [Flipping an Image](#flipping - an - image)

https://leetcode.com/problems/flipping-an-image/

``` python
def flipAndInvertImage(self, A: List[List[int]])->List[List[int]]:
    for i in range(len(A)) :
        if len(A[i]) % 2 != 0 :
            for j in range(len(A[i])//2+1):
                temp = A[i][j]
                A[i][j] = abs(A[i][len(A[i]) - j - 1] - 1)
                A[i][len(A[i]) - j - 1] = abs(temp - 1)
        else:
    for j in range(len(A[i])//2):
        temp = A[i][j]
        A[i][j] = abs(A[i][len(A[i]) - j - 1] - 1)
        A[i][len(A[i]) - j - 1] = abs(temp - 1)
return A
```