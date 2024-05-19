class MaxHeap:
    def __init__(self, arr=[]) -> None:
        self.heap = arr
        for i in range(len(arr)//2 - 1, -1, -1):
            self.heapify(i)

    def __str__(self) -> str:
        return str(self.heap)


    def insert(self, num):
        self.heap.append(num)

        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(i)

    def delete(self, num):
        delIndex = self.index_of(num)
        if delIndex == -1: # Not found deleted number
            return 
        
        self.heap[delIndex], self.heap[-1] = self.heap[-1], self.heap[delIndex]
        self.heap.pop()

        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, index):
        if index == len(self.heap) - 1: # Final leaf node have no child to heapify
            return

        largest = index
        n = len(self.heap)
        l_index = 2*index + 1
        r_index = 2*index + 2
        
        if l_index < n and self.heap[l_index] > self.heap[index]:
            largest = l_index
        if r_index < n and self.heap[r_index] > self.heap[largest]:
            largest = r_index
            
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest] # Swap
            self.heapify(largest)

    def sort(self) -> list[int]:
        n = len(self.heap)
        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            for j in range(n//2 - 1, -1, -1):
                self.heapify(j)

    # Return -1 if index not found, otherwise return number's located index
    def index_of(self, num):
        n = len(self.heap)
        index = -1
        for i in range(n):
            if self.heap[i] == num:
                index = i

        return index


heap = MaxHeap()
heap.insert(3)
heap.insert(9)
heap.insert(2)
heap.insert(1)
heap.insert(4)
heap.insert(5)
print(heap) # [9, 4, 5, 1, 3, 2]
heap.delete(4)
print(heap) # [9, 3, 5, 1, 2]

heap2 = MaxHeap([1, 3, 2, 4, 6, 5])
print(heap2)
heap2.sort()
print(heap2)
