"""
Counting Sort:
The Counting Sort algorithm sorts an array by counting the number of times each value occurs.

Counting Sort does not compare values like the previous sorting algorithms we have looked at, and only works on non negative integers.

Furthermore, Counting Sort is fast when the range of possible values k is smaller than the number of values n
"""

"""
Conditions for Counting Sort

Integer values: Counting Sort relies on counting occurrences of distinct values, so they must be integers. With integers, each value fits with an index (for non negative values), and there is a limited number of different values, so that the number of possible different values 
k is not too big compared to the number of values n.

Non negative values: Counting Sort is usually implemented by creating an array for counting. When the algorithm goes through the values to be sorted, value x is counted by increasing the counting array value at index x. If we tried sorting negative values, we would get in trouble with sorting value -3, because index -3 would be outside the counting array.

Limited range of values: If the number of possible different values to be sorted k is larger than the number of values to be sorted n, the counting array we need for sorting will be larger than the original array we have that needs sorting, and the algorithm becomes ineffective.
"""

# A 'countingSort' method that receives an array of integers.
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val+1)
    
    while len(arr) > 0:
        num = arr.pop(0)
        count[num]+=1
        
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
            
    return arr

# An array with values to sort.
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)

"""
Time Complexity:
How fast the Counting Sort algorithm runs depends on both the range of possible values k and the number of values n.

In general, time complexity for Counting Sort is O(n + k).

In a best case scenario, the range of possible different values k is very small compared to the number of values n and Counting Sort has time complexity O (n).

But in a worst case scenario, the range of possible different values k is very big compared to the number of values n and Counting Sort can have time complexity O(n^2) or even worse.
"""