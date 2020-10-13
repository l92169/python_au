# Linked list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)

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