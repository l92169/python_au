# Tree

## Kth Smallest Element in a BST

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

``` python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    A = []
    res = self.inord(root, A)
    return res[k - 1]


def inord(self, node, A):
        if node.left:
            self.inord(node.left, A)
        A.append(node.val)
        if node.right:
            self.inord(node.right, A)
        return A
```