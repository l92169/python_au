# Intervals

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

``` python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    arr = []
    def helper(i, root):
        if root:
            if i >= len(arr):
                arr.append([])
            arr[i].append(root.val)
            helper(i + 1, root.left)
            helper(i + 1, root.right)
    helper(0, root)
    return arr

```

