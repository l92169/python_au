# Tree

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)


## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

``` python
def __init__(self, root: TreeNode):
    self.index = -1
    self.arr = []
    self.helper(root)


def helper(self, root):
    if root == None:
        return
    self.helper(root.left)
    self.arr.append(root.val)
    self.helper(root.right)


def next(self) -> int:
    self.index += 1
    return self.arr[self.index]


def hasNext(self) -> bool:
    return self.index + 1 < len(self.arr)
```

