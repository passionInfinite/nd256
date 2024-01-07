import sys
import unittest


class Node:
    def __init__(self, character, frequency) -> None:
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        self.next = None
        self.prev = None


class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def enqueue(self, node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head

            while current_node.next and current_node.frequency < node.frequency:
                current_node = current_node.next

            # check if the prev is none then its the first element
            if current_node.prev is None:
                if current_node.frequency < node.frequency:
                    current_node.next = node
                    node.prev = current_node
                    node.next = None
                else:
                    current_node.prev = node
                    node.next = current_node
                    node.prev = None
                    self.head = node
            else:
                if current_node.frequency < node.frequency:
                    current_node.next = node
                    node.prev = current_node
                    node.next = None
                else:
                    prev_node = current_node.prev
                    prev_node.next = node
                    node.prev = prev_node
                    node.next = current_node
                    current_node.prev = node

        self.size += 1

    def dequeue(self):
        """
        Return head as it will be lowest frequency node in priority queue.
        """
        if self.head:
            node = self.head
            next_node = self.head.next
            if next_node:
                next_node.prev = None
            self.head = next_node
            self.size -= 1
            return node
        else:
            self.size = 0
            return None

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.character)
            current_node = current_node.next


class InvalidInputString(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class HuffmanEncoder:

    @staticmethod
    def build_character_frequency_dict(string):
        frequencies = dict()
        for character in string:
            if frequencies.get(character):
                frequencies[character] += 1
            else:
                frequencies[character] = 1
        return frequencies

    def build_priority_queue(self, string):
        queue = PriorityQueue()
        frequencies = self.build_character_frequency_dict(string)
        for character in frequencies:
            queue.enqueue(Node(character, frequencies.get(character)))
        return queue

    def get_code(self, huffman_tree, character):

        def recurse(node, character, code):
            if node.character == character:
                return code

            if node.left and character in node.left.character:
                code = recurse(node.left, character, code + "0")

            if node.right and character in node.right.character:
                code = recurse(node.right, character, code + "1")

            return code

        return recurse(huffman_tree, character, "")

    def display_huffman_tree(self, tree):
        if tree is None:
            return

        self.display_huffman_tree(tree.left)

        self.display_huffman_tree(tree.right)

    def encode(self, string):
        priority_queue = self.build_priority_queue(string)
        if priority_queue.size > 1:
            while priority_queue.size != 1:
                left_node = priority_queue.dequeue()
                right_node = priority_queue.dequeue()
                parent = Node(
                    left_node.character+right_node.character,
                    left_node.frequency+right_node.frequency
                )
                parent.left = left_node
                parent.right = right_node
                priority_queue.enqueue(parent)

            huffman_tree = priority_queue.dequeue()
            self.display_huffman_tree(huffman_tree)
            cache = dict()
            huffman_code = ""
            for character in string:
                if cache.get(character):
                    code = cache.get(character)
                else:
                    code = self.get_code(huffman_tree, character)
                    cache[character] = code

                huffman_code += code

            return huffman_code, huffman_tree
        else:
            raise InvalidInputString("Invalid string passed for encoding")

    def decode(self, encoded_data, huffman_tree):
        decoded_string = ""
        current_node = huffman_tree
        for bit in encoded_data:
            if bit == '1':
                current_node = current_node.right
            else:
                current_node = current_node.left

            if current_node.left is None and current_node.right is None:
                decoded_string += current_node.character
                current_node = huffman_tree

        return decoded_string


huffmanencoder = HuffmanEncoder()


# Test Case 1
input_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
print("\nThe size of the data is: {}".format(sys.getsizeof(input_string)))
encoded_data, huffman_tree = huffmanencoder.encode(input_string)
print("\nThe size of the encoded data is: {}".format(
    sys.getsizeof(int(encoded_data, base=2))))

decoded_data = huffmanencoder.decode(encoded_data, huffman_tree)
print("\nEncoded data is: {}".format(encoded_data))
print("\nDecoded data is: {}".format(decoded_data))
assert input_string == decoded_data

# Test Case 2 empty input string passed
input_string = ""
try:
    huffmanencoder.encode(input_string)
except InvalidInputString:
    assert True

# Test Case 3 passing long input string with only one character must be throwing input error as we need minimum of two leaf nodes to build huffman tree
input_string = "".join(["A" for _ in range(10000)])
try:
    huffmanencoder.encode(input_string)
except InvalidInputString:
    assert True
