"""
Quicksort Algorithm:

Takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.
"""

def partition(array,low,high):
    pivot=array[high]
    i=low-1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
            
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array,low=0,high=None):
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_index = partition(array,low,high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)
        
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

"""
Time Complexity:

The worst case scenario for Quicksort is 
O(n^2). This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, this happens when the array is already sorted.

But on average, the time complexity for Quicksort is actually just 
O(n log n), which is a lot better than for the previous sorting algorithms we have looked at. That is why Quicksort is so popular.

Below you can see the significant improvement in time complexity for Quicksort in an average scenario 
O(n log n), compared to the previous sorting algorithms Bubble, Selection and Insertion Sort with time complexity 
O(n2)
"""