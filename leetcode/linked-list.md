# Linked list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

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

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def reverse(self, head: ListNode):
    cur = head
    prev = None
    next = None
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
def lenght(self, head:ListNode):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
def isPalindrome(self, head:ListNode) -> int:
    first = head
    second = self.reverse(head)
    for i in range(self.lenght(head)):
        if first.val != second.val:
            return False
        else:
            first = first.next
            second = second.next
    return True

```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    cur = output = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return output.next
```