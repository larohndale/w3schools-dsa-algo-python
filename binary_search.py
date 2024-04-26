"""
Binary Search Algorithm:
Searches through an array and returns the index of the value it searches for and relies on the fact the list has to be sorted

If our list is not sorted binary search may return None 
 """

def binary_search(list,target):
    # Constant Runtime
    first = 0
    last = len(list)-1
    
    #  // is a floor division operator rounding down 
    while first <= last:
        midpoint = (first + last)//2   
        
        # Best case scenario
        # Constant runtime
        if list[midpoint] == target: 
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
            
    return None

# Function to verify if the given index is found in the list
def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in the list")
        
# Define list
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 6)
verify(result)

"""
Time Complexity:
Each time Binary Search checks a new value to see if it is the target value, the search area is halved.

This means that even in the worst case scenario where Binary Search cannot find the target value, it still only needs 
log
2
n
 comparisons to look through a sorted array of 
n
 values.

Time complexity for Binary Search is

O(log2n)

Binary Search is constant or O(1) i.e. O(n) which is logarithmic
"""    