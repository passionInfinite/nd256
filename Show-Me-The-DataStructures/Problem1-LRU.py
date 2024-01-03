# This class represent the cache node that will be used with double linked / cache bucket
class CacheNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()

        self.head = None  # Head represents the least recently used cache item
        self.tail = None  # Tail represents the Most recently used cache item
        self.capacity = capacity
        self.size = 0

    # This function rearrages the element that we are getting to the tail of the DLL to mark it as Most Recently Used element.
    def moveToTail(self, key):
        node = self.cache[key]
        prevNode = node.left
        nextNode = node.right
        if prevNode:
            prevNode.right = nextNode
        if nextNode:
            nextNode.left = prevNode
        del self.cache[key]
        self.size -= 1

    # This function removes the LRU cache element from the DLL and move the head pointer
    def removeHead(self):
        if self.head:
            self.head = self.head.right
            self.head.left = None
            self.size -= 1

    def set(self, key, value):
        node = CacheNode(key, value)
        # print(self.size, self.capacity)
        if self.size >= self.capacity:
            # Calling this will always remove the least recently used from the linked list.
            self.removeHead()
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.size += 1
        else:
            self.tail.right = node
            node.left = self.tail
            self.tail = node
            self.size += 1

        self.cache[key] = self.tail

    def get(self, key):
        # First check in cache and if exists return from cache
        try:
            node = self.cache[key]
            self.moveToTail(key)
            self.set(node.key, node.value)
            return node.value
        except:
            return -1


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))
print(our_cache.get(6))
