"""
Insertion Sort:

The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)
    
print("Sorted Array: ", my_array)

# Insertion Sort Improvement by swapping instead of shifting
array2 = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(array2)
for i in range(1,n):
    insert_index = i
    current_value = array2[i]
    for j in range(i-1, -1, -1):
        if array2[j] > current_value:
            array2[j+1] = array2[j]
            insert_index = j
        else:
            break
    array2[insert_index] = current_value
    
print("Improved sorted array: ", array2)

"""
Time Complexity:

On average, each value must be compared to about n/2 other values to find out where to insert it.

And Selection Sort must run the loop to insert a value in its correct place approximately n times.

We get time complexity for Insertion Sort:

O(n2⋅n)= O(n2)
"""