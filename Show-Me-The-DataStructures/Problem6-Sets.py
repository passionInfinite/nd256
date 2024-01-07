class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def values(self):
        valuesList = []
        current_node = self.head
        while current_node:
            valuesList.append(current_node.value)
            current_node = current_node.next
        return valuesList


def generateLinkedList(values):
    """
    Helper function to generate linked list

    :params: values
    :return: LinkedList
    """
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)

    return linked_list


def union(llist_1, llist_2):
    finalList = llist_1.values()
    finalList.extend(llist_2.values())
    return generateLinkedList(set(finalList))


def intersection(llist_1, llist_2):
    setOne = set(llist_1.values())
    setTwo = set(llist_2.values())

    if len(setTwo) < len(setOne):
        # switch shorter set to setA as intersection set will be lesser in length
        setOne, setTwo = setTwo, setOne

    intersectionValues = [num for num in setOne if num in setTwo]
    return generateLinkedList(intersectionValues)


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
llist1 = generateLinkedList([1, 2, 3, 4, 5])
llist2 = generateLinkedList([])
assert union(llist1, llist2).values() == llist1.values()
assert intersection(llist1, llist2).values() == llist2.values()


# Test Case 2
llist1 = generateLinkedList([])
llist2 = generateLinkedList([])
assert union(llist1, llist2).values() == []
assert intersection(llist1, llist2).values() == []

# Test Case 3
llist1 = generateLinkedList([1, 2, 3, 4, 4, 5, 5])
llist2 = generateLinkedList([1, 2, 3, 4, 5, 5])

assert union(llist1, llist2).values() == [1, 2, 3, 4, 5]
assert intersection(llist1, llist2).values() == [1, 2, 3, 4, 5]
