# Array

+ [Max Consecutive Ones](#max-consecutive-ones)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

``` python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxx, count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if count > maxx:
                maxx = count
            count = 0
    if count > maxx:
        maxx = count
    return maxx
```
