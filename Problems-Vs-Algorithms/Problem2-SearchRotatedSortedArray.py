def find_pivot(input_list, left, right):
    # if the search is exhausted that means the roatation has never happened.
    if right < left:
        return -1

    if left == right:
        return left

    mid = (left + right) // 2

    if mid < right and input_list[mid] > input_list[mid+1]:
        return mid

    if mid > left and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[left] >= input_list[mid]:
        return find_pivot(input_list, left, mid - 1)
    return find_pivot(input_list, mid+1, right)


def binary_search(input_list, left, right, number):

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
