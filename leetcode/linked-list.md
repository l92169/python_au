# Linked List

## Intersection of Two Linked Lists

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

https://leetcode.com/problems/intersection-of-two-linked-lists/

``` python
def length(self, head):
    lengt = 0
    while head:
        head = head.next
        lengt += 1
    return lengt
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    hA = headA
    hB = headB
    lenA = self.length(headA)
    lenB = self.length(headB)
    delt = lenA - lenB
    while delt > 0:
        hA = hA.next
        delt -= 1
    while delt < 0:
        hB = hB.next
        delt += 1
    while hA != hB:
        hA = hA.next
        hB = hB.next
    return hA
```