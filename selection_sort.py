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
    