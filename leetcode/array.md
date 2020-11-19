# Array

## Reshape the Matrix

+ [Reshape the Matrix](#reshape-the-matrix)

https://leetcode.com/problems/reshape-the-matrix/

``` python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    new_arr = []
    res = [[0]*c for i in range(r)]
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            new_arr.append(nums[i][j])
    count = 0
    for i in range(r):
        for j in range(c):
            if count < len(new_arr):
                res[i][j] = int(new_arr[count])
            else:
                return nums
                break
            count += 1
    return(res)
```