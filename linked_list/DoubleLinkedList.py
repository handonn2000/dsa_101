class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        return f"{self.val}"

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, None, None)
        self.tail = Node(0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __str__(self):
        current = self.head 
        display = ""
        while current:
            display += str(current.val) + " <-> "
            current = current.next
        return display + f"\nsize = {self.size}"
    
    def get(self, pos):
        if self.size == 0 or pos < 0 or pos > self.size:
            return None
        
        mid = self.size / 2
        currentNode = None
        if pos < mid:
            currentNode = self.getHeadNode()
            while pos > 0:
                currentNode = currentNode.next
                pos -= 1
        else:
            currentNode = self.getTailNode()
            while pos > 0:
                currentNode = currentNode.prev
                pos -= 1
        return currentNode

    def getHeadNode(self):
        return self.head.next
    
    def getTailNode(self):
        return self.tail.prev

    def insert(self, pos, val):
        if pos < 0 or pos > self.size:
            print("Index out of range")
            return
        
        if pos == 0:
            if self.size == 0:
                self.head.next = Node(val, self.head, self.tail)
                self.tail.prev = self.getHeadNode()
            else:
                currHeadNode = self.getHeadNode()
                self.head.next = Node(val, self.head, currHeadNode)
        elif pos == self.size:
            currTailNode = self.getTailNode()
            self.tail.prev = Node(val, currTailNode, self.tail)
            currTailNode.next = self.getTailNode()
        else:
            prevNode = self.get(pos - 1)
            afterNode = prevNode.next
            prevNode.next = Node(val, prevNode, afterNode)
        
        self.size += 1

    def remove(self, pos):
        if pos < 0 or pos > self.size or self.size == 0:
            print("Index out of range")
            return
        
        if pos == 0:
            curHeadNode = self.getHeadNode()
            afterNode = curHeadNode.next
            self.head.next = curHeadNode.next
            afterNode.prev = self.head
        else:
            prevNode = self.get(pos - 1)
            currentNode = prevNode.next
            prevNode.next = prevNode.next.next
            currentNode.prev = currentNode.prev
        self.size -= 1

    def contains(self, val):
        currentNode = self.getHeadNode()
        while currentNode != self.tail and currentNode.val != val:
            currentNode = currentNode.next

        return True if currentNode != self.tail else False

myList = DoubleLinkedList()
myList.insert(0, 1)
myList.insert(0, 2)
myList.insert(2, 3)
myList.insert(1, 4)
myList.insert(2, 5)
print(myList)
myList.remove(1)
print(myList)
myList.remove(0)
print(myList)
myList.remove(2)
print(myList)
print(myList.contains(1))
print(myList.contains(10))