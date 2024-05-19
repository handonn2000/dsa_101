class HeapSort:
    def __init__(self, arr) -> None:
        self.arr = arr
    def __str__(self) -> str:
        return str(self.arr)
    
    def sort(self):
        n = len(self.arr)

        # Build max heap
        for i in range(n//2-1, -1, -1):
            self._heapifydown(n, i)

        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i] # Swap max to end
            self._heapifydown(i, 0)

    def _heapifydown(self, n, index):
        while True:
            largest = index
            lIndex = 2*index + 1
            rIndex = 2*index + 2

            if lIndex < n and self.arr[lIndex] > self.arr[largest]:
                largest = lIndex
            if rIndex < n and self.arr[rIndex] > self.arr[largest]:
                largest = rIndex

            if largest != index:
                self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
                index = largest
            else:
                break


heap_sort = HeapSort([1, 3, 6, 5, 9, 8, 0])
heap_sort.sort()
print(heap_sort)