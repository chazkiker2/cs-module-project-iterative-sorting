# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # select sort is REALLY slow
    # going to select and compare things one at a time
    # if current element is smaller than compared element, swap the two and repeat

    # START EASIER APPROACH
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # starts at first — stops at second to last
        cur_index = i  # for the sake of readability/clarity
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):  # starts at el after i — stops at very end
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    # END EASIER APPROACH (TYPING-WISE)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # bubble_sort is slightly faster than selection_sort
    for i in range(len(arr)):  # all the way to the end in first loop
        for j in range(0, len(
                arr) - i - 1):  # all the way to the almost end, then subtract above index (ignore final index)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


# EXAMPLE OF COUNTING_SORT:
# arr=[1,2,3,3,5,3]
# maximum=5
# counting_sort(arr, maximum):::
# output_bucket = [0] * maximum => [0] * 5 => [0, 0, 0, 0, 0]
# count_bucket = [0] * len(arr) => [0] * 6 => [0, 0, 0, 0, 0, 0]
#
# for i in arr:  # for each el in input arr
#   count_bucket[i] += 1  # (see below)
# --- count_bucket[1] += 1 => count_bucket==[0, 1, 0, 0, 0, 0]
# --- count_bucket[2] += 1 => count_bucket==[0, 1, 1, 0, 0, 0]
# --- count_bucket[3] += 1 => count_bucket==[0, 1, 1, 1, 0, 0]
# --- count_bucket[3] += 1 => count_bucket==[0, 1, 1, 2, 0, 0]
# --- count_bucket[5] += 1 => count_bucket==[0, 1, 1, 2, 0, 1]
# --- count_bucket[3] += 1 => count_bucket==[0, 1, 1, 3, 0, 1]
#
#  for i in range(maximum):  # change count[] to contain the position of this element
#         count_bucket[i] += count_bucket[i-1]  # (see below)
# --- maximum=5, so for i in range(5) => 0, 1, 2, 3, 4, 5
# --- count_bucket[0] += count_bucket[i-1] => count_bucket[0] += count_bucket[-1] => count_bucket[0]


def counting_sort(arr):
    # initialize array to MAX in arr
    if len(arr) == 0:
        return []

    maximum = int(max(arr))
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    output_bucket = [0] * len(arr)  # another way to do this: [0 for _ in range(arr)]
    # if len(arr)=6, output_bucket = [0, 0, 0, 0, 0, 0]

    count_bucket = [0] * (maximum + 1)  # if max=5, count_bucket = [0, 0, 0, 0, 0, 0]

    for el in arr:
        count_bucket[el] += 1  # put the count of instances in the count[] at the index that IS the number in question

    # then, count num of instances of each number
    for i in range(1, len(count_bucket)):
        # change count[] to contain the position of this element
        count_bucket[i] += count_bucket[i - 1]

    # reconstruct the output_bucket
    for i in range(len(arr) - 1, -1, -1):
        output_bucket[count_bucket[arr[i]] - 1] = arr[i]
        count_bucket[arr[i]] -= 1

    # actually change input array
    for i in range(0, len(arr)):
        arr[i] = output_bucket[i]

    return arr  # then return mutated array back to client

    # this algo is hard to memorize, but it is incredibly fast for sorting
    # certainly much faster than both of the above algorithms
    # time complexity is O(n)
    # but this sacrifices memory to be so fast (which is okay, because it's fast)


def count_sort_with_negatives(arr):
    if len(arr) == 0:
        return []

    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    # create a count array to store count of individual elements
    # and initialize count array as o for each element
    output_bucket = [0] * len(arr)  # empty slot for each of the number of elements in input arr
    count_bucket = [0] * range_of_elements  # empty slot for each of the range of elements

    # for i in range(0, len(arr)):
    #    count_bucket[arr[i] - min_element] += 1

    for el in arr:
        count_bucket[el - min_element] += 1

    for i in range(1, len(count_bucket)):
        count_bucket[i] += count_bucket[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_bucket[count_bucket[arr[i] - min_element] - 1] = arr[i]
        count_bucket[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_bucket[i]

    return arr

# # Driver program to test count_sort_with_negatives function
# arr_1 = [-5, -10, 0, -3, 8, 5, -1, 10]
# ans = count_sort(arr_1)
# print("Sorted character array is " + str(ans))
