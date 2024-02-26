def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i = 0
    j = 0
    k = len(input_list) - 1

    while j <= k:

        if input_list[j] == 0:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j += 1

        elif input_list[j] == 1:
            j += 1

        else:
            input_list[j], input_list[k] = input_list[k], input_list[j]
            k -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([1, 2, 0]) # all three position needs swapping

test_function([0, 1, 2]) # by default sorted

test_function([2, 1, 0]) # needs sorting for first and last only
