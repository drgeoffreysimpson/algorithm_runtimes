# Constant Runtime
def OddorEven(n):
    return "Even" if n % 2 else "Odd"

import time
start = time.time()

retval = OddorEven(5)

end = time.time()
print(f"OddOrEven: {(end - start):.10f}")


# Logarithmic time
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

import random

b = list(range(1,99999))
start = time.time()

retval = binarySearch(b, 2)

end = time.time()

print(f"binary search: {(end - start):.10f}")


# Linear time
# find largest number in unsorted list

def findmax(a):
    max_item = a[0]
    for item in a:
        if item > max_item:
            max_item = item

a = list(range(1, 9999))
random.shuffle(a)

start = time.time()

for x in range (1,10000):
    output = findmax(a)

end = time.time()

print(f"findmax: {(end - start):.10f}")


# Polynomial time
# bubbl sort
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
    
        # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]
arr = list(range(1,999999))
random.shuffle(arr)

start = time.time()
output = bubbleSort(a)

end = time.time()

print(f"bubble sort: {(end - start):.10f}")

# Exponential 
# finding all the subsets of a set

from itertools import chain, combinations

def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

start = time.time()
output = subsets(range(1,99999999))
end = time.time()

print(f"find all subsets: {(end - start):.10f}")


# for each, add data and/or executions and graph the results

