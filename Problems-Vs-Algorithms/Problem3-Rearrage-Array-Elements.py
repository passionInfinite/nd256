# perform heapsort
def sort(arr):
    """
    Sorting function to perform heap sort
    Args:
        arr(list): list to sort using heap.
    Return:
        None: As in place sorting is done
    """
    arr_len = len(arr)

    for i in range(arr_len - 1, -1, -1):
        heapification(arr, len(arr), i)

        # Swap the top element in heap with last element in array
        arr[0], arr[i] = arr[i], arr[0]


def heapification(arr, n, i):
    """
    :param: arr - array for heapification
    n(int): number of elements
    i(int): index of the current element
    """
    for i in range(1, i + 1):
        # Perform heapify
        data_index = i
        while data_index > 0:
            parent_index = (data_index - 1) // 2
            if arr[data_index] > arr[parent_index]:
                arr[data_index], arr[parent_index] = arr[parent_index], arr[data_index]
                data_index = parent_index
            else:
                break


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # check if input list is empty
    if len(input_list) <= 1:
        return []

    # perform heapsort
    sort(input_list)

    num_1 = list()
    num_2 = list()
    n = len(input_list)

    # If the no. of digits is odd, then set the first digit of the first number as
    if n % 2 == 1:
        digit = input_list.pop()
        num_1.append(str(digit))

    n = len(input_list)
    # Append the digits in input list to the 2 numbers in an interleave manner
    for i in range(n, 0, -1):
        digit = input_list.pop()
        if i % 2 == 0:
            num_1.append(str(digit))
        else:
            num_2.append(str(digit))

    # Return both numbers as integers after joining
    return [int(''.join(num_1)), int(''.join(num_2))]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])  # empty array as input and output should be []
test_function([[1], []]) # with only one element we cannot create two maximum sums.