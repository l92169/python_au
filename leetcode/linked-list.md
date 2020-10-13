# Linked list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    next = None
    cur = head
    while cur!=None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return  prev
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    array = [head]
    while array[-1].next!=None:
        array.append(array[-1].next)
    return array[len(array)//2]

```