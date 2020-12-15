# Tree

+ [Validate Binary Search Tree](#validate-binary-search-tree)

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

``` python
def isValidBST(self, root: TreeNode) -> bool:
    def recursion(node, mn = float('-inf'), mx = float('inf')):
        if not node:
            return True
        if node.val <= mn or node.val >= mx:
            return False
        return (recursion(node.right, node.val, mx) and recursion(node.left, mn, node.val))
    return recursion(root)
```