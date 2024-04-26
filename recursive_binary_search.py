# Recursive Binary Search
# Recursive function is a function that calls itself 
# A number of times a recursive function calls itself is Recursion Depth
# Iterate usually means a loop but recursion is slightly different as it has stopping points
# Binary Search is runs at O(log n) logarithmic time constant space

def recursive_binary_search(list,target):
    # Base Case
    # Must check if the list is empty as recursive functions call themselves (splitting in half) essentially resulting with an empty list or array
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:                # 
                return recursive_binary_search(list[:midpoint],target)

def verify(result):
    print("Target found : ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers,12)
verify(result)

result = recursive_binary_search(numbers,6)
verify(result)

