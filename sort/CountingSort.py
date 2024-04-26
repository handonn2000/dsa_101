"""
Idea:
    Count element in the array and find max
    Create a count[] with size max
    Calculate the prefix sum of count[]
    For each num in the original array:
        + k = get value in position num then - 1
        + update k to that position
        + ans[k] = num
Note: 
    Counting sort cannot be used with negative number
    Couting sort is a stable sort algo -> since it maintain the original order of a sorted element

TC: O(n + max) with n = len(nums)
SC: O(max)
"""
class CountingSort:
    def sort(self, nums: list[int]) -> list[int]:
        countDict = dict()
        max = nums[0]
        for num in nums:
            if num > max:
                max = num
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1

        countArr = [0] * (max + 1)
        for num, count in countDict.items():
            countArr[num] = count

        for num, count in enumerate(countArr):
            if num == 0: continue
            countArr[num] += countArr[num - 1]

        ans = [0] * len(nums)
        for num in nums:
            countArr[num] -= 1
            k = countArr[num]
            ans[k] = num
        
        return ans

assert CountingSort().sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

# assert CountingSort().sort([3,7,2,-4,9]) == [-4,2,3,7,9]
assert CountingSort().sort([5,4,3,2,1]) == [1,2,3,4,5]
assert CountingSort().sort([3,7,2,4,9]) == [2,3,4,7,9]
assert CountingSort().sort([3,7,2,2,9]) == [2,2,3,7,9]
assert CountingSort().sort([1,2,3,4,5]) == [1,2,3,4,5]
assert CountingSort().sort([2,1]) == [1,2]
assert CountingSort().sort([1]) == [1]

print("All tests passed")