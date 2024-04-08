# LIFO: last in first out
# Stack don't have th ability in random access
class SimpleStack:
    def __init__(self) -> None:
        self.storage = []
    def __str__(self) -> str:
        return str(self.storage)

    # O(1)
    def push(self, val) -> None:
        self.storage.append(val)

    # O(1)
    def pop(self) -> any:
        return self.storage.pop() # Or remove & get last element

    # O(1)
    def peek(self) -> any:
        return self.storage[-1]
    
    # O(1)
    def isEmpty(self) -> bool:
        return len(self.storage) == 0
    


myStack = SimpleStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)
print(myStack.storage)
# myStack.pop()
# print(myStack)
# print(myStack.peek())
# myStack.push(4)
# print(myStack)
# print(myStack.isEmpty())
# myStack.pop()
# myStack.pop()
# myStack.pop()
# print(myStack.isEmpty())

