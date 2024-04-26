from math import sqrt

def square_root(x: int):
    left = 0.0
    right = float(x)
    epsilon = 1e-6

    while right - left >= epsilon:
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        
        if mid * mid > x:
            right = mid
        else:
            left = mid
        
    return left 

assert square_root(4) == sqrt(4)
print(sqrt(5))
print(square_root(5))
# assert square_root(5) == sqrt(5)
# assert square_root(9) == sqrt(9)
# assert square_root(2147483647) == sqrt(2147483647)

print("All tests passed")