# in linear search, start at beginning and iterate
# through one at a time until you've found the target
#
# very efficient if the target is towards the START
# very inefficient if the target is towards the END
def linear_search(arr, target):
    # solution 1
    for index, element in enumerate(arr):  # for each {index, element} in arr
        if element == target:
            return index

    # both the above and below solutions are the same for time complexity
    # the only difference is readability
    # (the above might be slightly faster, though)

    # solution 2
    if target in arr:  # if target is inside arr
        return arr.index(target)  # return the index of that target

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # binary is a BETTER SEARCH METHOD than linear_search
    # take a tree, cut it in half, look to left and look to right and
    # take whichever half is the better fit for your target.
    # then, repeat until you have found your target
    # (or, until you have exhausted all options in which case target is not in list)

    # this will take roughly half the time of linear_search

    # we are NOT using recursion
    left = 0  # initial left index
    right = len(arr) - 1  # initial right index

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:  # if element at middle is target
            return middle  # return middle index
        elif arr[middle] > target:  # else if element at middle is GREATER THAN target
            right = middle - 1  # decrease right index in order to take left half
        else:  # else, element at middle is less than target
            left = middle + 1  # increase left index in order to take RIGHT half

    return -1  # not found
