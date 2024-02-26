import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return ()

    minimum = ints[0]
    maximum = ints[0]

    for i in range(1, len(ints)):
        if minimum > ints[i]:
            minimum = ints[i]

        if maximum < ints[i]:
            maximum = ints[i]

    return (minimum, maximum)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [0, 9, 8, 2, 3, 40, -1]
print("Pass" if ((-1, 40) == get_min_max(l)) else "Fail")

# edge cases
l = []
random.shuffle(l)
print("Pass" if (() == get_min_max(l)) else "Fail")

l = [1, 1, 1, 1]
random.shuffle(l)
print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
