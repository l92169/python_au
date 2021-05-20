# Dynamic programming

+ [House Robber](#house-robber)

## House Robber

https://leetcode.com/problems/house-robber/

``` python
def rob(self, nums: List[int]) -> int:
    length = len(nums)
    if length == 0:
        return 0
    elif length == 1:
        return nums[0]
    elif length == 2:
        return max(nums)
    else:
        summ = [0]*length # assign dp array
        summ[0], summ[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            summ[i] = max(summ[i-1], summ[i-2]+nums[i])
        return max(summ)
```