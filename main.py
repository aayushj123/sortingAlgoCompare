import time
import math
import random
import matplotlib.pyplot as plt

#different number of elements in array
n = [10, 100, 1000, 5000, 10000, 20000, 50000, 100000]

inputArr = []
bubbleTime = []
insertionTime = []
selectionTime = []
mergeTime = []
quickTime = []

def bubbleSort(Array):
    size = len(Array)
    for i in range(size):
        for j in range(size - i - 1):
            if Array[j] > Array[j + 1]:
                temp = Array[j]
                Array[j] = Array[j + 1]
                Array[j + 1] = temp

def selectionSort(Array):
    size = len(Array)
    for i in range(size):
        minElemIndex = i
        for j in range(i + 1, size):
            if (Array[minElemIndex] > Array[j]):
                minElemIndex = j
        temp = Array[minElemIndex]
        Array[minElemIndex] = Array[i]
        Array[i] = temp

def insertionSort(Array):
    size = len(Array)
    for i in range(1, size):
        key = Array[i]
        j = i - 1
        while j >= 0 and Array[j] > key:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = key


def mergeSort(Array, p, r):
    def combine(Array, p, q, r):
        leftArraySize = q - p + 1
        rightArraySize = r - q
        leftArray = [None] * (leftArraySize + 1)
        rightArray = [None] * (rightArraySize + 1)
        for i in range(leftArraySize):
            leftArray[i] = Array[p + i]
        for j in range(rightArraySize):
            rightArray[j] = Array[q + j + 1]
        leftArray[leftArraySize] = math.inf
        rightArray[rightArraySize] = math.inf
        i = 0
        j = 0
        for k in range(p, r + 1):
            if (leftArray[i] < rightArray[j]):
                Array[k] = leftArray[i]
                i = i + 1
            else:
                Array[k] = rightArray[j]
                j = j + 1

    if (p < r):
        q = (p + r) // 2
        mergeSort(Array, p, q)
        mergeSort(Array, q + 1, r)
        combine(Array, p, q, r)


def quickSort(Array, p, r):
    def partition(Array, p, r):
        pivotElem = Array[r]
        i = p - 1

        for j in range(p, r):
            if (Array[j] < pivotElem):
                i = i + 1
                temp = Array[i]
                Array[i] = Array[j]
                Array[j] = temp

        temp = Array[i + 1]
        Array[i + 1] = Array[r]
        Array[r] = temp
        return i + 1

    if (p < r):
        partitionPoint = partition(Array, p, r)
        quickSort(Array, p, partitionPoint - 1)
        quickSort(Array, partitionPoint + 1, r)

for j in n:
    for i in range(j):
        ele = random.randint(0, 1000000)
        inputArr.append(ele)

    #Bubble Sort
    start = time.time()
    bubbleSort(inputArr)
    end = time.time()
    bubbleTime.append(round(end - start, 4))

    #Selection Sort
    start = time.time()
    selectionSort(inputArr)
    end = time.time()
    selectionTime.append(round(end - start, 4))

    #Insertion Sort
    start = time.time()
    insertionSort(inputArr)
    end = time.time()
    insertionTime.append(round(end - start, 4))

    #Merge Sort
    start = time.time()
    mergeSort(inputArr, 0, j - 1)
    end = time.time()
    mergeTime.append(round(end - start, 4))

    #Quick Sort
    start = time.time()
    mergeSort(inputArr, 0, j - 1)
    end = time.time()
    quickTime.append(round(end - start, 4))


print(bubbleTime, insertionTime, selectionTime, mergeTime, quickTime)

#graph
plt.xlabel('Number of elements')
plt.ylabel('Time Taken (in sec)')
plt.title('Time required by different Sorting Algorithms')
plt.plot(n, bubbleTime, label = "bubbleSort")
plt.plot(n, insertionTime, label = "insertionSort")
plt.plot(n, selectionTime, label = "selectionSort")
plt.plot(n, mergeTime, label = "mergeSort")
plt.plot(n, quickTime, label = "quickSort")

plt.legend()
plt.show()