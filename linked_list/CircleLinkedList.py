class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next 
    def __str__(self):
        return f"{self.val}"

class CircleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current = None
        self.size = 0
    def __str__(self) -> str:
        return f"{self.current}"

    def add(self, val) -> None:
        newNode = Node(val, None)
        if self.size == 0:
            self.current = newNode
            self.head = self.current
        else:
            newNode.next = self.head
            self.current.next = newNode
            self.current = self.current.next      

        self.size += 1     

    def remove(self, pos) -> None:
        if pos == 0:
            self.head = self.head.next
        else:
            beforeRemoveNode = self.head
            for _ in range(pos - 1):
                beforeRemoveNode = beforeRemoveNode.next

            if pos == self.size - 1:
                beforeRemoveNode.next = self.head
                self.current = beforeRemoveNode
            else:
                beforeRemoveNode.next = self.current

        self.current.next = self.head
        self.size -= 1
            

    # O(1)
    def getFirst(self) -> Node:
        print("head: ", self.head)
        return self.head

    # O(1)
    def getLast(self) -> Node:
        print("last: ", self.current)
        return self.current


cList = CircleLinkedList()
cList.add(1)
cList.add(2)
cList.add(3)
cList.add(4)
cList.add(5)
cList.getFirst() # 1
cList.getLast() # 5

cList.remove(0)
cList.getFirst() # 2

cList.remove(3)
cList.getLast() # 4
print(cList.current)

cList.remove(1)
cList.getFirst() # 2
cList.getLast() # 4
print(cList.current)


