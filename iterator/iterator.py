class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.count:
            return -1
        else:
            cur = self.head
            while index > 0:
                cur = cur.next
                index -= 1
            return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
        self.count += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        elif index == self.count:
            return self.addAtTail(val)
        elif index < 0 or index >= self.count:
            return
        else:
            newNode = Node(val)
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
            self.count += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)