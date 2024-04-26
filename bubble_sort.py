"""
Bubble Sort: Sorts an array from the lowest value to the highest value.

The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.
"""
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range (n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            
print('Sorted array: ', my_array)

# Bubble sort improvement
my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in (range(n-i-1)):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break
    
print("Bubble sorted array enhanced ", my_array)

"""
Time Complexity: 
The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. So for an array of n values, there must be n such comparisons in one loop.

And after one loop, the array is looped through again and again n times.

This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is:

O(n2)
"""