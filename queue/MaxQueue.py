from collections import deque

class MaxQueue:
    def __init__(self) -> None:
        self.q = deque()
        self.mq = deque()
    def __str__(self) -> str:
        return str(self.q) + " - " + str(self.mq)

    def enqueue(self, val: int) -> None:
        self.q.append(val)
        if len(self.mq) == 0:
            self.mq.append(val)

        while self.mq and self.mq[-1] <= val:
            self.mq.pop()
        self.mq.append(val)

    def dequeue(self) -> int:
        if self.mq and self.q[0] == self.mq[0]:
            self.mq.popleft()
        return self.q.popleft()

    def getMax(self) -> int:
        print(self.mq[0])
        return self.mq[0]

queue = MaxQueue()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(3)
queue.getMax()
queue.dequeue()
queue.getMax()
queue.enqueue(1)
queue.getMax()
queue.enqueue(5)
queue.getMax()
print(queue)