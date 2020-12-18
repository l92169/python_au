# Linked list

## Remove Nth Node From End of List

+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

``` python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    length, count = 0, 0
    cur = head
    prev = head
    while cur != None:
        cur = cur.next
        length = length + 1
    delt = length - n
    if delt == 0:
        prev = head.next
        return prev
    while (count != delt - 1 and delt > 0):
        head = head.next
        count = count+1
    if head.next.next != None:
        head.next = head.next.next
        return prev
    else:
        head.next = None
        return prev
```