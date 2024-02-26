def find_pivot(input_list, left, right):
    """
    find pivot where the array is rotated
    Args:
       input_list(list): list of rotated integers
       left(int): left index ptr
       right(int): right index ptr
    Returns:
       int: Pivot of the index where the array is rotated.
    """
    # if the search is exhausted that means the roatation has never happened.
    if right < left:
        return -1

    if left == right:
        return left

    mid = (left + right) // 2

    # check if mid is less then the right ptr and the value of mid index in input is greater than the value of mid+1 in input_list.Return mid
    if mid < right and input_list[mid] > input_list[mid+1]:
        return mid
    # check if mid is greater then the left ptr and the value of mid index in input is less than the value of mid-1 in input_list. Return mid-1
    if mid > left and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    # check if the value of element at index left ptr and mid ptr then continue finding the pivot in left to mid-1
    if input_list[left] >= input_list[mid]:
        return find_pivot(input_list, left, mid - 1)

    # otherwise continue finding pivot in mid+1 to right
    return find_pivot(input_list, mid+1, right)


def binary_search(input_list, left, right, number):
    """
    Performs binary search within the input list.
    Args:
       input_list(list): list of rotated integers
       left(int): left index ptr
       right(int): right index ptr
       number: target to check against for search range
    Returns:
       int: Pivot of the index where the array is rotated.
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    if number < input_list[mid]:
        return binary_search(input_list, left, mid - 1, number)
    elif number > input_list[mid]:
        return binary_search(input_list, mid+1, right, number)
    else:
        return mid


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find pivot index where the rotation has happended
    pivotIndex = find_pivot(input_list, 0, len(input_list) - 1)

    if pivotIndex == -1:
        return pivotIndex

    # once pivot index is found check if that element at that index is the target number.
    if input_list[pivotIndex] == number:
        return pivotIndex

    # check if first element of the input list is lt target that means our element is in left sorted array
    if input_list[0] <= number:
        # search in the left half
        return binary_search(input_list, 0, pivotIndex - 1, number)
    else:
        # search in the right half
        return binary_search(input_list, pivotIndex+1, len(input_list) - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])  # if array is empty return should be -1
# if array is not rotated return should be -1
test_function([[1, 2, 3, 5, 8, 7, 6], -1])
