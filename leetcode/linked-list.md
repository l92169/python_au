#Linked list

+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)

##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    array = [head]
    while array[-1].next!=None:
        array.append(array[-1].next)
    return array[len(array)//2]
```

##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    cur = None
    for i in range(self.length(head)//2):
        head = head.next
    return head 
def length(self, head):
    count = 0
    while head != None:
        head = head.next
        count += 1
    return count
```
