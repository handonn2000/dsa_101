"""
Idea: From each element in the array, find the smallest one, then move it to the left

TC: O(n^2)
SC: O(1)
"""
class SelectionSort:
    def sort(nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            min_pos = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_pos]:
                    min_pos = j
            nums[i], nums[min_pos] = nums[min_pos], nums[i]
    
        return nums


assert SelectionSort.sort([3,7,2,4,9]) == [2,3,4,7,9]
assert SelectionSort.sort([3,7,2,-4,9]) == [-4,2,3,7,9]
assert SelectionSort.sort([3,7,2,2,9]) == [2,2,3,7,9]
assert SelectionSort.sort([1,2,3,4,5]) == [1,2,3,4,5]
assert SelectionSort.sort([5,4,3,2,1]) == [1,2,3,4,5]
assert SelectionSort.sort([2,1]) == [1,2]
assert SelectionSort.sort([1]) == [1]

print("All tests passed")