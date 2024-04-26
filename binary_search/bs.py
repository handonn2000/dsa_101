# Iterative Method
def i_binary_search(arr: list[int], target: int) -> bool:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        if target < arr[mid]:
            right = mid - 1
        if target > arr[mid]:
            left = mid + 1
    return False

# Recursive Method
def r_binary_search(arr: list[int], left: int, right: int, target: int) -> bool:
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        if target < arr[mid]:
            return r_binary_search(arr, left, mid - 1, target)
        if target > arr[mid]:
            return r_binary_search(arr, mid + 1, right, target)
    else:
        return False

arr1 = [1,2,3,4,5,6,8,9,10]
for i in range(1, 11):
    print("Iterative: ", i, i_binary_search(arr1, i))
print("-"*20)
for i in range(1, 11):
    print("Recursive: ", i, r_binary_search(arr1, 0, len(arr1) - 1, i))

print("All tests passed")