import time

########## Instruction
# 1. Rear about quick sort
# 2. Read about divide and conquer
# 3. Get the following code to run

def partition(arr, low, high):
    # Write you code here - set i to the lowest element

    #

    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Write your code here - increment index of smaller element

            #
            # Write your code here, swap arr[i] and arr[j]

            #

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # part is partitioning index, arr[p] is now at right place
        part = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

a=[1,2,4,100,5,2,7,100,1,1000,200,3,56,4e8,6,2]

tstart = time.time()
for i in range(10000):
    quickSort(a, 0, len(a) - 1)
tend = time.time()
runtime1 = tend-tstart
print('Run time for Insertion Sort =',runtime1,'s')

tstart = time.time()
for i in range(10000):
    a.sort()
tend = time.time()
runtime2 = tend-tstart
print('Run time for Python Defualt sort =',runtime2,'s')

print('Your algorithm is',runtime1 / runtime2, 'time slower than the python default algorithm')