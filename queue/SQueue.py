class SQueue:

    def __init__(self):
        self.s1 = []

    def __str__(self) -> str:
        return str(self.s1)

    def push(self, x: int) -> None:
        temp = []
        while self.s1:
            temp.append(self.s1.pop())
        self.s1.append(x)
        while temp:
            self.s1.append(temp.pop())
        
    def pop(self) -> int:
        return self.s1.pop()
    
    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


queue = SQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue)
print(queue.pop())
print(queue.pop())
