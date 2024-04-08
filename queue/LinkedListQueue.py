class QueueNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

class LKQueue:
    def __init__(self, capacity) -> None:
        self.front = None
        self.rear = None
        self.size = 0
        self.capacity = capacity
    def __str__(self) -> str:
        return str(self.front)

    def enqueue(self, val):
        if self.isFull():
            print("Queue full: pls dequeue to add more")
            return

        queueNode = QueueNode(val)
        if self.size == 0:
            self.front = queueNode
            self.rear = self.front
        else:
            current = self.rear
            self.rear = queueNode
            current.next = self.rear
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue empty: pls add more item")
            return None
        dequeueVal = self.front.val
        self.front = self.front.next
        self.size -= 1
        return dequeueVal

    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
queue = LKQueue(5)
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.rear.val)
print(queue.front.val)
queue.dequeue()
queue.dequeue()
print(queue)