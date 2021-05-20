# Linked list

+ [Merge k Sorted Lists](#merge-k-sorted-lists)

## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

``` python
def mergeTwoLists(self, l1, l2):
    cur = output = ListNode()
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 == None:
        cur.next = l2
    if l2 == None:
        cur.next = l1
    return output.next

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    a, b = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
    return self.mergeTwoLists(a, b)
```

