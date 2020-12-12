# Tree

## Invert Binary Tree

+ [Invert Binary Tree](#invert-binary-tree)

https://leetcode.com/problems/invert-binary-tree/

``` python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root == None:
        return None
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

```