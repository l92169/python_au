#Linked List

+ [Palindrome Linked List](#palindrome-linked-list)

##Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

``` python
def isPalindrome(self, head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    FT = True
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            FT = False
    return(FT)
```
