class MinStack:
    def __init__(self) -> None:
        self.storage = []
        self.ms = []
    def __str__(self) -> str:
        print("ms: ", self.ms, "| min: ", self.getMin())
        return "s " + str(self.storage)

    # O(1)
    def push(self, val) -> None:
        self.storage.append(val)
        if len(self.ms) == 0 or self.ms[-1] >= val:
            self.ms.append(val)

    # O(1)
    def pop(self) -> any:
        if self.storage[-1] == self.ms[-1]:
            self.ms.pop()
        return self.storage.pop()
    
    # O(1)
    def getMin(self) -> any:
        return self.ms[-1]

myStack = MinStack()
myStack.push(5)
myStack.push(1)
myStack.push(7)
myStack.push(3)
myStack.push(1)
myStack.push(10)
myStack.push(0)

print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)
