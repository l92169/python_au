#Linked List

##Merge Two Sorted Lists

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

https://leetcode.com/problems/merge-two-sorted-lists/

``` python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
```