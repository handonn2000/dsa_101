import random 

class QuickSort:
    def partition(self, nums: list[int], left: int, right: int, pivotIndex: int) -> int:
        pivot = nums[pivotIndex]
        while left <= right: 
            while nums[left] < pivot: 
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:  
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        return left


    def quick_sort(self, nums: list[int], start: int, end: int) -> None:
        if end - start <= 0:
            return
        
        pivotIndex = end
        partitionIndex = self.partition(nums, start, end - 1, pivotIndex)

        self.quick_sort(nums, start, partitionIndex - 1)
        self.quick_sort(nums, partitionIndex + 1, end)
        
    def sort(self, nums: list[int]) -> list[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        print(nums)
        return nums
    

assert QuickSort().sort([1,8,5,9,4,3,7]) == [1,3,4,5,7,8,9]
assert QuickSort().sort([3,7,2,-4,9]) == [-4,2,3,7,9]
assert QuickSort().sort([5,4,3,2,1]) == [1,2,3,4,5]
assert QuickSort().sort([3,7,2,4,9]) == [2,3,4,7,9]
assert QuickSort().sort([3,7,2,2,9]) == [2,2,3,7,9]
assert QuickSort().sort([1,2,3,4,5]) == [1,2,3,4,5]
assert QuickSort().sort([2,1]) == [1,2]
assert QuickSort().sort([1]) == [1]


print("All tests passed")