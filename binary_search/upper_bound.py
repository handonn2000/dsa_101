# Return last index of target in the arr (-1 if not found)
def upper_bound(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2
        if target >= arr[mid]:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

assert upper_bound([1,2,3,4,6,6,6,8], 6) == 6
assert upper_bound([1,2,2,4,6,6,6,8], 2) == 2
assert upper_bound([1,1,3,4,6,6,6,8], 1) == 1
assert upper_bound([1,2,3,4,6,6,8,8], 8) == 7

print("All tests passed")