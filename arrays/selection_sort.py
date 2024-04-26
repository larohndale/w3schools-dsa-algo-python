"""
Selection Sort:
Goes through all elements in an array, finds the lowest value, and moves it to the front of the array, and does this over and over until the array is sorted.


"""

# Selection Sort Implementation
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1):
    print("array initialized", my_array)
    print("i becomes min_index: ", i)
    print("n: ", n, "n-1: ", n-1)
    min_index = i
    for j in range(i+1, n):
        print("array value: ", my_array[j])
        print("j: ", j)
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
    print("Array sorting: ", my_array)
        
print("Sorted array:", my_array)

# Improve selection sort by swapping the lowest value and first value instead of shifting
my_array_swap = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array_swap)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array_swap[j] < my_array_swap[min_index]:
            min_index = j
    # Notice we swap the values of i and min_index
    my_array_swap[i], my_array_swap[min_index] = my_array_swap[min_index], my_array_swap[i] 
    
print("Swapped Sorted Array: ", my_array_swap)
    
"""
Time Complexity:

Selection Sort goes through an array of n values n−1 times. This is because when the algorithm has sorted all values except the last, the last value must also be in its correct place.

The first time the algorithm runs through the array, every value is compared to find out which one is the lowest.

The second time the algorithm runs through the array, every value except the first value is compared to find out which is the lowest.

And in this way the unsorted part of the array becomes shorter and shorter until the sorting is done. So on average, n/2 elements are considered when the algorithm goes through the array finding the lowest value and moving it to the front of the array.

Using Big O notation to describe the time complexity for the Selection Sort algorithm, we get:

O(1/2⋅n2)= O(n2)

"""