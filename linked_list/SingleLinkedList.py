from enum import Enum

class SortDirection(Enum):
    ASC = 1
    DES = 2

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val} -> {self.next}"
    
class SingleLinkedList:
    def __init__(self):
        self.head = Node(0, None) # sentinel node
        self.size = 0
    def __len__(self):
        return self.size
    def __str__(self):
        return f"value = [{str(self.head.next)}]\nsize = {self.size}\n---"
    
    def get(self, pos) -> Node:
        if pos < 0 and pos >= self.size:
            print("Index out of range")
            return None
        currentNode = self.getHeadNode()
        while pos > 0 and currentNode.next != None:
            currentNode = currentNode.next
            pos -= 1
        return currentNode
    
    def getHeadNode(self) -> Node:
        if self.size == 0:
            print("LinkedList has 0 element")
            return None
        return self.head.next
    
    def push(self, val):
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = Node(val, None)
        self.size += 1

    def insert(self, pos, val):
        if pos < 0 and pos > self.size:
            print("Index out of range")
            return

        if pos == 0:
            currentHeadNode = self.getHeadNode()
            self.head.next = Node(val, currentHeadNode)
        else:
            prevNode = self.get(pos - 1)
            currentPosNode = prevNode.next
            prevNode.next = Node(val, currentPosNode)
        self.size += 1

    def remove(self, pos):
        if pos < 0 and pos >= self.size:
            print("Index out of range")
            return
        
        if pos == 0:
            headNode = self.getHeadNode()    
            self.head.next = headNode.next
        else:
            prevNode = self.get(pos - 1)
            prevNode.next = prevNode.next.next
        self.size -= 1

    def contains(self, val):
        currentNode = self.getHeadNode()
        while currentNode != None and currentNode.val != val:
            currentNode = currentNode.next

        return True if currentNode != None else False

    def sort(self, sortDirection: SortDirection):
        arr = self.toArray()
        if sortDirection == SortDirection.DES:
            arr.sort(reverse=True)
        elif sortDirection == SortDirection.ASC:
            arr.sort(reverse=False)
        else:
            raise Exception("Only accept ASC or DES")
        sortedLinkedList = self.fromArray(arr)
        self.head = sortedLinkedList.head
        self.size = sortedLinkedList.size

    def toArray(self) -> list[int]:
        arr = [0] * self.size
        currentNode = self.getHeadNode()
        for pos in range(self.size):
            arr[pos] = currentNode.val
            currentNode = currentNode.next
        return arr
    
    @classmethod
    def fromArray(cls, arr):
        myList = cls()
        for val in arr:
            myList.push(val)
        return myList

myList = SingleLinkedList()
myList.push(1)
myList.push(2)
myList.push(3)
myList.push(4)
myList.push(5)
print(myList)
print(myList.get(0).val)
print(myList.get(1).val)
myList.insert(0, 0)
myList.insert(5, 6)
print(myList)
print(myList.contains(10))
print(myList.toArray())

list2 = SingleLinkedList.fromArray([5,7,2,1,0,3])
list2.sort(SortDirection.DES)
print(list2)

list2.remove(0)
list2.remove(1)
print(list2)