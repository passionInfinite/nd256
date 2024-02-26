import re

# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for subpath in parts:
            if subpath not in node.children:
                node.insert(subpath)
            node = node.children[subpath]

        node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        for subpath in parts:
            if subpath not in node.children:
                return None
            else:
                node = node.children[subpath]

        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, subpath):
        # Insert the node as before
        self.children[subpath] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, rootHandler, notFoundHandler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie()
        self.add_handler("", rootHandler)
        self.notFoundHandler = notFoundHandler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.router.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.router.find(self.split_path(path))
        if handler is None:
            return self.notFoundHandler
        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        # this will clean up both first and last '/' so we always start clean
        path = re.sub(r"/+", '/', path) # this helps to replace duplicate slashes
        path = path.strip('/')
        return path.split('/')


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))


# some more edge cases
print(router.lookup("//"))  # should print root handler
print(router.lookup("///"))  # should still print root handler
# should return about handler because the replace is handling the duplicate slashes
print(router.lookup("/home///about//"))
