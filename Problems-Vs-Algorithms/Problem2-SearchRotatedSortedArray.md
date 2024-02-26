To locate the index from where the array was rotated we can use binary search algorithm with following 3 conditions.

For each iteration of binary search algorithm, the middle element was checked against three conditions:
1. The array was rotated in a way that the mid value is larger than both the left and right value.
2. The array was rotated in a way that the mid value is smaller than both the left and right value.
3. The array was not at all rotated.

Based on the above three conditions we return the mid. This will be the pivot index. Then we use this pivot index and compare the value at pivot index in input list with the target value. If smaller then we look in the left side of the array or else right side of the array using binary search.

The time complexity for this program is O(logn) and space complexity is O(1) as it is using constant space.