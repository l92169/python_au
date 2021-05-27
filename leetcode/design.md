# Design

+ [Implement Stack using Queues](#implement-stack-using-queues)

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

``` python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.q1 = deque()
    self.q2 = deque()
    self._top = None


def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    self.q1.append(x)
    self._top = x


def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    while len(self.q1) > 1:
        self._top = self.q1.popleft()
        self.q2.append(self._top)
    temp = self.q1.popleft()
    self.q1, self.q2 = self.q2, self.q1
    return temp


def top(self) -> int:
    """
    Get the top element.
    """
    return self._top


def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return len(self.q1) == 0
```

