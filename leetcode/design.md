# Design

+ [Implement Queue using Stacks](#implement-queue-using-stacks)

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

``` python

def __init__(self):
    self.queue = []


def push(self, x: int) -> None:
    self.queue.append(x)


def pop(self) -> int:
    new = self.queue[0]
    self.queue.pop(0)
    return new


def peek(self) -> int:
    return self.queue[0]


def empty(self) -> bool:
    if self.queue == []:
        return True
    else:
        return False
```

