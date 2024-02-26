We stored the subpath as the keys in the Trie Class and TrieNode consist of two flags the children which was using another trienode with the next subpath. The other flag for TrieNode is the handler for that until that subpath.

The additional responsibility of defining the root handler and the route not found handler is given to the Router class.

The `split_path` function defines the logic behind generating parts from the actual supplied string path. This function takes care of duplicate `/` as well as it trims the staring and trailing slashes. So the root path `/` will become `''` in Trie. That gives us flexibility to tackle all the edge cases.

The `lookup` function utilizes the `find` of the Trie class going through all the subpaths until the end is reach. If in between any not found subpath exists then we return `None` otherwise the `handler` is returned. Further, we check if `None` is returned from the `find` function then we return `not found handler` which is defined on the Router class other the actual `handler` is returned.

The time complexity for this program is O(m) where m is the number of subpaths in the path splitted by '/' Whereas the space complexity for this program is O(path_lengths * no of unique subpaths * no of paths)

