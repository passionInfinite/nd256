In this solution, I have used below data structures:
1. Priority Queue using DoublyLinkedList: This stores the nodes starting from min frequency to max frequency. while enqueuing it always inserts in the place according to the sorted order by swapping elements.
2. Used Dictionary for leveraging caching while generating the codes by searching into the huffman tree. if the search for a specific character is already done we save it in dictory with key being character and value being the character prefix code. This helps to avoid multiple lookups in the huffman tree for a specific character.
Used Tree Structure to build the huffman tree based on the queue dequeuing nodes.

The time complexity for this solution is:
To build the frequency table is `O(n)` where n is the total no of characters from the input string.
To build the priority queue is `O(m)` where m is unique characters in the input string
To build the tree is also `O(2m - 1)`

so worst case time complexity is `O(n)`

Decoding part takes worst case time complexity of O(logn) to traverse the tree and generate the codes. The space complexity for this solution is
1. To store m unique characters from the input string in priority queue is O(m)
2. To generate the huffman tree takes O(m)
3. To store cache for the prefix codes will be O(m) where m remains unique characters.
So overall the space complexity will be O(m) where m is the unique elements from the input string but in worst case scenario where all the characters are unique the space complexity will become O(n) where n is number of elements in the input string.