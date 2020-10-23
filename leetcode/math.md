# Math

## Reverse Integer

+ [Reverse Integer](#reverse-integer)

https://leetcode.com/problems/reverse-integer/

``` python
def reverse(self, x: int) -> int:
    a = 0
    if x == 0:
        return x
    elif x < 0:
        x = x * (-1)
        while x != 0:
            a = a * 10 + x % 10
            x = x // 10
        return a * (-1)
    else:
        while x != 0:
            a = a * 10 + x % 10
            x = x // 10
        return a
```