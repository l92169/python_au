# Linked list

## Reorder List

+ [Reorder List](#reorder-list)

https://leetcode.com/problems/reorder-list/

``` python
ass ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
s Solution:
def reverse_list(self, head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def get_middle_of_list(self, head):
    if head is None:
        return head

    slow = head
    fast = head
    prev_slow = None
    while fast is not None and fast.next is not None:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    if fast is None:
        prev_slow.next = None
        return slow
    else:
        res = slow.next
        slow.next = None
        return res


def merge_lists(self, left, right):
    cur_left = left
    cur_right = right

    while cur_left is not None and cur_right is not None:
        next_left = cur_left.next
        next_right = cur_right.next

        cur_left.next = cur_right
        cur_right.next = next_left

        cur_left = next_left
        cur_right = next_right

    return left


def reorderList(self, head):
    prev_middle = self.get_middle_of_list(head)
    first = head
    second = prev_middle
    second = self.reverse_list(second)
    head = self.merge_lists(first, second)
```