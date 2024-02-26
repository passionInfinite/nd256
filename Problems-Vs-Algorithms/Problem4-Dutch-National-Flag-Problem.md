Using three pointers (i, j, k) to keep track of the last inserted element of value 0, 1, 2 respectively.

Simply iterate over the elements starting index trackers with (i, j, k) = (0, 0, n-1) where n is length of the array. Using three conditions perform swaping of the values at those indexes and increment those indexes.

1. if element at index j == 0, then swap element at index i and index j.
2. if element at index j == 1, no need to perform swapping just increment the j tracking index.
3. if element at index j != 0 and element at index j != 1, swap j and k and decrement the tracker k.

The end result will be the correct result array.

The time complexity for this program is O(n) as we iterate over the array once using three indexes. Whereas the space complexity for this program is O(n) as all the swapping happens in place.