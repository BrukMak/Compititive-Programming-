class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or self.head == None:
            return -1
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        else:
            new_node = Node(val)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif index > self.size:
            return
        else:
            new_node = Node(val)
            cur_node = self.head
            for _ in range(index-1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            
        self.size += 1
        return
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            cur = self.head
            self.head = cur.next
            
        elif index < self.size:
            cur_node = self.head
            for _ in range(index-1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
            
        self.size -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)