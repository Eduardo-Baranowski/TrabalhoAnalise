# Python program for implementation of Bubble Sort
import random, time, psutil, sys
ini = time.time()

arr100000 = []
while len(arr100000) < 100000:
     n = random.randrange(100000)
     if n not in arr100000:
        arr100000.append(n)




'''


arr100 = []
while len(arr100) < 100:
     n = random.randrange(1000)
     if n not in arr100:
        arr100.append(n)

arr10000 = []
while len(arr10000) < 10000:
     n = random.randrange(10000)
     if n not in arr10000:
        arr10000.append(n)

print(len(arr10000))

arr100000 = []
while len(arr100000) < 100000:
     n = random.randrange(100000)
     if n not in arr100000:
        arr100000.append(n)

print(len(arr100000))
'''

def bubbleSort(arr):
    comp = 0
    troca = 0
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):
            comp+=1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                troca+=1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('comp', comp)
    print('troca', troca)

def insertionSort(arr):
    comp = 0
    insert = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        comp+=1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                insert+=1
        arr[j+1] = key
    print(comp)
    print(insert)






# Traverse through all array elements
troca = 0
comp = 0
for i in range(len(arr100000)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(arr100000)):
        comp+=1
        if arr100000[min_idx] > arr100000[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    arr100000[i], arr100000[min_idx] = arr100000[min_idx], arr100000[i]
    troca+=1

print(comp)
print(troca)
'''
# Driver code to test above
print ("Sorted array")
for i in range(len(arr100)):
    print("%d" %arr100[i]),


insertionSort(arr100000)
print ("Sorted array is:")
for i in range(len(arr100000)):
    print ("%d" %arr100000[i])

bubbleSort(arr100000)

print ("Sorted array is:")
for i in range(len(arr100000)):
    print ("%d" %arr100000[i]),

bubbleSort(arr10000)

print ("Sorted array is:")
for i in range(len(arr10000)):
    print ("%d" %arr10000[i]),

bubbleSort(arr100000)

print ("Sorted array is:")
for i in range(len(arr100000)):
    print ("%d" %arr100000[i]),


fim = time.time()
cpu = psutil.cpu_times()
print('aqui ', psutil.virtual_memory())
print("Tempo ", fim - ini)
print('cpu ', cpu)
print('aqui ', psutil.cpu_percent())
for i in range(int(fim-ini)):
        print(psutil.cpu_percent())


'''