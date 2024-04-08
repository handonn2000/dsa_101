# Find next greater element of each element in the array
# Store index of next greater element, if None store -1
# Input: [1,5,3,7,9]
# Output: [1,3,3,4,-1]

"""
Brute-force:
    - 2 for loop: one for iterate through all element i, one iterate from i + 1 until it find next greater element
    - TC: O(n^2) and SC: O(1)
Idea: 
    - Notice in the above example output, some value is the same
        + 7 is next great element of both 5, 3 --> every element after 5 and smaller has 7 is the next great

"""
def skyLine(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)

    stack = []
    for pos, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            ans[stack.pop()] = pos 
        stack.append(pos)

    return ans
    
# print(skyLine([1,5,3,7,9]))
assert skyLine([1,5,3,7,9]) == [1,3,3,4,-1]
assert skyLine([1,5,3,2,4,9]) == [1,5,4,4,5,-1]
print("Tests passed")