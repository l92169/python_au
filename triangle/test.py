class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next s
class Solution:
    def reverseList(self) -> ListNode:
        head = 1->2->3->4->5->NULL
        prev = None
        next = None
        cur = head
        while cur!=None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return  prev
if __name__ == "__main__":
    print(Solution.reverseList())
