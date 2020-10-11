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