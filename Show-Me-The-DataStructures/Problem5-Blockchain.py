import hashlib
import time


class Node:
    def __init__(self, block):
        self.block = block
        self.next = None


class Block:
    def __init__(self, timestamp, data, previous_hash) -> None:
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addBlock(self, data):
        previous_hash = None

        if self.tail:
            previous_hash = self.tail.block.hash

        node = Node(Block(time.time(), data, previous_hash))

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node


# Test Case 1
blockchain = BlockChain()
blockchain.addBlock('Hi this is my first block')
blockchain.addBlock('Hi this is my second block')

assert (blockchain.head is not None)
assert blockchain.head.block.hash == blockchain.tail.block.previous_hash

# Test Case 2
blockchain = BlockChain()
blockchain.addBlock('') # data is empty

assert blockchain.head.next == None
assert blockchain.head.block.hash is not None
 
# add one more block
blockchain.addBlock('Hi this is second block')
assert blockchain.head.block.hash == blockchain.tail.block.previous_hash

# Test Case 2
blockchain = BlockChain()
blockchain.addBlock('Hello')
blockchain.addBlock('Hi')
assert isinstance(blockchain.head, Node)
assert isinstance(blockchain.head.block, Block)
assert isinstance(blockchain.tail, Node)
assert isinstance(blockchain.tail.block, Block)
assert blockchain.head.next is not None
assert blockchain.tail.next is None