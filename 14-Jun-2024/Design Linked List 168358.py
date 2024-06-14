# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            curr = curr.next
            if curr == None:
                return -1
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return 

        temp = self.head
        while temp.next:
            temp = temp.next
    
        temp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(-1,self.head)
        temp = dummy
        node = Node(val)
        for i in range(index):
            temp = temp.next
            if temp == None:
                self.head = dummy.next
                return 
    
        if temp:
            node.next = temp.next
            temp.next = node
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(-1,self.head)
        temp = dummy
        for i in range(index):
            temp = temp.next
            if temp == None:
                self.head = dummy.next
                return None
    
        if temp and temp.next:
            temp.next = temp.next.next
        self.head = dummy.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)