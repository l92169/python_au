# Array

## Move Zeroes

+ [Move Zeroes](#move-zeroes)

https://leetcode.com/problems/move-zeroes/

``` python
def moveZeroes(self, nums: List[int]) -> None:
    count = 0
    while 0 in nums:
        nums.remove(0)
        count += 1
    for i in range(count):
        nums.append(0)
    return nums
```