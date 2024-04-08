from collections import deque

class MinQueue:
    def __init__(self) -> None:
        self.q = deque()
        self.minq = deque()
    def __str__(self) -> str:
        return str(self.q) + str(self.minq)

    def enqueue(self, val: int) -> None:
        self.q.append(val)
        while self.minq and val < self.minq[-1]:
            self.minq.pop()
        self.minq.append(val)
    
    def dequeue(self) -> int:
        if self.minq and self.minq[0] == self.q[0]:
            self.minq.popleft()
        return self.q.popleft()

    def getMin(self) -> int:
        print(self.minq[0])
        return self.minq[0]
    
queue = MinQueue()
queue.enqueue(4)
queue.getMin()
queue.enqueue(2)
queue.enqueue(3)
queue.getMin()
queue.enqueue(1)
queue.getMin()
print(queue)