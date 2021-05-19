# Design 

+ [Min Stack](#min-stack)

## Min Stack

https://leetcode.com/problems/min-stack/

``` python

def __init__(self):
    self.stack = []
    self.minn = []


def push(self, val: int) -> None:
    self.stack.append(val)
    minn = self.minn
    minn.append(val if not minn else min(val, minn[-1]) )


def pop(self) -> None:
    self.stack.pop()
    self.minn.pop()


def top(self) -> int:
    return self.stack[-1]


def getMin(self) -> int:
    return self.minn[-1]
```

