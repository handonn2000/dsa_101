from collections import deque

class SimpleQueue:
    def __init__(self, capacity) -> None:
        self.queue = deque()
        self.capacity = capacity

    def __str__(self) -> str:
        return str(self.queue)
    
    def enqueue(self, val):
        if self.isFull():
            print("Queue full")
            return
        self.queue.appendleft(val)

    def dequeue(self):
        if self.isEmpty():
            print("Queue Empty") 
            return
        self.queue.pop()

    def isFull(self):
        return len(self.queue) == self.capacity
    
    def isEmpty(self):
        return len(self.queue) == 0


myQueue = SimpleQueue(3)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue)
print(myQueue.isFull())
myQueue.enqueue(4)
myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
myQueue.dequeue()
print(myQueue)
print(myQueue.isEmpty())
myQueue.dequeue()
