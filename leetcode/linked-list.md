#Linked list

##Middle of the Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    array = [head]
    while array[-1].next!=None:
        array.append(array[-1].next)
    return array[len(array)//2]
```