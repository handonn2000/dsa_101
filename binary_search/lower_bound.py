# Return first index of target in the array (-1 if not found)
def lower_bound(arr: list[int], target) -> int:
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left)//2
        if target <= arr[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

assert lower_bound([1,2,3,4,6,6,6,8], 6) == 4
assert lower_bound([1,2,2,4,6,6,6,8], 2) == 1
assert lower_bound([1,1,3,4,6,6,6,8], 1) == 0
assert lower_bound([1,2,3,4,6,6,8,8], 8) == 6

print("All tests passed")