# Array

## Squares of a Sorted Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

https://leetcode.com/problems/squares-of-a-sorted-array/

``` python
def get_first_nonnegative(self, A: List[int]):
    for i, val in enumerate(A):
        if val >= 0:
            return i
    return -1
def sortedSquares(self, A: List[int]) -> List[int]:
    ind = self.get_first_nonnegative(A)
    if ind == -1:
        return [x ** 2 for x in A[::-1]]
    elif ind == 0:
        return [x ** 2 for x in A]
    else:
        left, right = ind - 1, ind
        length = len(A)
        res = []
        while right < length and left >= 0:
            if A[left] ** 2 < A[right] ** 2:
                res.append(A[left] ** 2)
                left -= 1
            else:
                res.append(A[right] ** 2)
                right += 1
        while left >= 0:
            res.append(A[left] ** 2)
            left -= 1
        while right < length:
            res.append(A[right] ** 2)
            right += 1
        return res
```