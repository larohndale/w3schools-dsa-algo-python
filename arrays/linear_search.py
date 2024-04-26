"""
Linear Search:

Compares each value with the value it is looking for. If the value is found, the index is returned, and if it is not found -1 is returned.
"""

# Linear Search Algorithm - O(n)
# """ < python docs standards
def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

# Function to verify if the given index is found in the list
def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in the list")
        
# Define list
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)
result = linear_search(numbers, 6)
verify(result)

"""
Time Complexity:

Best Case Scenario is if the value we are looking for is the first value in the array. In such a case only one compare is needed and the time complexity is 
O(1)

Worst Case Scenario is if the whole array is looked through without finding the target value. In such a case all values in the array are compared with the target value, and the time complexity is 
O(n)

Average Case Scenario is not so easy to pinpoint. What is the possibility to finding the target value? That depends on the values in the array right? But if we assume that exactly one of the values in the array is equal to the target value, and that the position of that value can be anywhere, the average time needed for Linear Search is half of the time time needed in the worst case scenario.

Time complexity for Linear Search is 
O(n)
"""