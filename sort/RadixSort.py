"""
Idea:
    Find max
    Iteration through list and divide max with 10 until it = 0
    Start sorting the last digits of each number (using stable sort)
    Continue sorting with the 2th, 3th, ... n-th last digits of each number
    If the place-th doesn't exist, count it as 0

TC: 
SC:
"""
from functools import cmp_to_key

class RadixSort:
    
    def sort(self, nums: list[int]) -> list[int]:
        max = nums[0]
        for num in nums:
            if num > max: 
                max = num

        k = 1
        while max > 0:
            def compare(num1, num2):
                n1 = len(str(num1)) - k
                digit1 = 0
                if n1 >= 0: 
                    digit1 = str(num1)[n1]

                n2 = len(str(num2)) - k
                digit2 = 0
                if n2 >= 0: 
                    digit2 = str(num2)[n2]
                if int(digit1) >= int(digit2):
                    return 1
                return -1 
            
            nums = sorted(nums, key=cmp_to_key(compare))
            k += 1
            max //= 10

        return nums
    

assert RadixSort().sort([53, 89, 150, 36, 633, 233]) == [36, 53, 89, 150, 233, 633]
assert RadixSort().sort([5,4,3,2,1]) == [1,2,3,4,5]
assert RadixSort().sort([3,7,2,4,9]) == [2,3,4,7,9]
assert RadixSort().sort([3,7,2,2,9]) == [2,2,3,7,9]
assert RadixSort().sort([1,2,3,4,5]) == [1,2,3,4,5]
assert RadixSort().sort([2,1]) == [1,2]
assert RadixSort().sort([1]) == [1]

print("All tests passed")