class MinHeap:
    def __init__(self, arr=[]) -> None:
        self.heap = arr
        self._heapify()
    def __str__(self) -> str:
        return str(self.heap)

    def heappush(self, num):
        self.heap.append(num)

        n = len(self.heap)
        self._siftup(n-1)

    def heappop(self):
        if len(self.heap) == 0:
            return -1
        
        min = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        
        self._siftdown(0)
        print(min)
        return min

    def array(self) -> list[int]:
        return self.heap.copy()

    def _heapify(self, arr=None):
        if arr is None:
            arr = self.heap

        n = len(arr)
        for i in range(n//2)[::-1]:
            self._siftdown(i)

    # O(logn)
    def _siftup(self, index, arr=None):
        if arr is None:
            arr = self.heap

        while index > 0:
            parent = (index - 1) // 2
            if arr[index] < arr[parent]:
                arr[parent], arr[index] = arr[index], arr[parent]
                index = parent
            else:
                break

    # O(logn)
    def _siftdown(self, index, arr=None):
        if arr is None:
            arr = self.heap

        n = len(arr)
        while True:
            minIndex = index
            lIndex = 2*index + 1
            rIndex = 2*index + 2

            if lIndex < n and arr[lIndex] < arr[minIndex]:
                minIndex = lIndex
            if rIndex < n and arr[rIndex] < arr[minIndex]:
                minIndex = rIndex
            
            if minIndex != index:
                arr[minIndex], arr[index] = arr[index], arr[minIndex]
                index = minIndex
            else:
                break



if __name__ == "__main__":
    heap = MinHeap()
    heap.heappush(1)
    heap.heappush(3)
    heap.heappush(6)
    heap.heappush(5)
    heap.heappush(9)
    heap.heappush(8)
    heap.heappush(0)
    print(heap) # [0, 3, 1, 5, 9, 8 ,6]
    heap.heappop() # 0
    print(heap) # [1, 3, 6, 5, 9, 8]

    heap2 = MinHeap([1, 3, 6, 5, 9, 8, 0])
    print(heap2)
    sorted_arr = heap2.sort()
    print(sorted_arr)