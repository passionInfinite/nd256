import math


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        number = int(number)
    except ValueError:
        return None
    
    # check for negative numbers as well
    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    start = 1
    end = number

    while start <= end:
        # using binary search to calc mid and update ranges accordingly.
        mid = (start+end) // 2

        if mid * mid < number:
            start = mid + 1
        elif mid * mid > number:
            end = mid - 1
        else:
            return mid

    return math.floor(end)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (5 == sqrt(25)) else "Fail")
print("Pass" if (sqrt(-2) == None) else "Fail")
print("Pass" if (sqrt("-2") == None) else "Fail")
print("Pass" if (sqrt(0) == 0) else "Fail")
