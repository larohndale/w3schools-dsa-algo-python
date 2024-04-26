"""
Array: An array is a data structure used to store multiple elements.
"""


# Find the lowest value in an array
my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value: ', minVal) 

"""
Time Complexity: 
In the example below, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is because the algorithm must visit every array element one time to find the lowest value. The loop must run 5 times since there are 5 values in the array. And if the array had 1000 values, the loop would have to run 1000 times.
"""