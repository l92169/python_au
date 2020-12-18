#Math

+ [Fibonacci Number](#fibonacci-number)
+ [Fibonacci Number](#fibonacci-number)

##Fibonacci Number

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

##Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

``` python
def fib(self, N: int) -> int:
        res = [0,1]
        if N == 0:
            return res[0]
        elif N == 1:
            return res[1]
        for i in range(2, N + 1):
            res.append(res[-1] + res[-2])            
        return res[-1]
```
