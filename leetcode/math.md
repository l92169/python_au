#Math

##Fibonacci Number

+ [Fibonacci Number](#fibonacci-number)

https://leetcode.com/problems/fibonacci-number/

``` python
def fib(self, N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N > 1:
        return(self.fib(N-1) + self.fib(N-2))
```