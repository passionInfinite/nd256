In this solution I have used 3 datastructures:
1. List to have input linked lists values as list
2. Set to have distinct values for the corresponding list of values
3. Linked List to convert the union or intersection lists to the linked list output.

The time complexity for this solution is converting the linked lists to lists for both the input sets is `O(2n)` and then preparing sets is `O(2n-m)` where m is the duplicate values and lastly Union function will have `O(n + m)` where n is the unique elements from set one and m is the unique elements from set two. Converting this final list to linked list is `O(n+m)` total number of elements in the set.
The worst case time complexity of union and intersection function is `O(n+m)` where n is the number of elements in first list and m is number of elements in second lists.

The space complexity will be O(n+m) where n is the number of elements in the linked list one and another one is number of elements in the linked list two. With this if both the sets has same sets of data then the space complexity becomes O(n).