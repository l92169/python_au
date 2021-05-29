# Math

+ [Base 7](#base-7)

## Base 7

https://leetcode.com/problems/base-7/

``` python
def convertToBase7(self, num: int) -> str:
    new_int = ''
    k = 1
    if num < 0:
        num = num * -1
        k = -1
    if num == 0:
        return '0'
    else:
        while num != 0:
            new_int = new_int + str(num % 7)
            num = num // 7
        new_int = new_int[::-1]
        return(str(int(new_int)*k))
```
