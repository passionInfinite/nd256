To store the words I have used the concept of tries. With the TrieClass having all the required functions to perform operations on the trie and TrieNode that stores the character with value being another TrieNode and a flag to denote whether that character depecits the end of the word formation.

I have used recursion concept to find all the suffixes from the trie that until we have iterated over all the character of the search input. With the recursion we keep adding the suffixes whenever the tri node has is_word flag as true. The base case for recursion to end is when there is no more children of the trienode to visit.

The time complexity for finding the suffix is O(n) where n is the number of characters in the word and space complexity is the O(word_length * non repeating characters * no of words)

