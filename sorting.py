#1.Pseudocode untuk merge sort
#function mergeSort(array):
#     if array has 1 or no elements:
#         return array
#     else:
#         divide array into two halves
#         left = mergeSort(left half)
#         right = mergeSort(right half)
#         return merge(left, right)

# function merge(left, right):
#     create an empty list result
#     while left and right are not empty:
#         if left[0] <= right[0]:
#             append left[0] to result and remove it from left
#         else:
#             append right[0] to result and remove it from right
#     append remaining elements of left (if any) to result
#     append remaining elements of right (if any) to result
#     return result
#--------------------KOMPLEKSITAS-------------------------------------
#BIG O
# -Splitting array : O(log n)
# -Merge step : O(n)
# -Total time complexity : O(n log n)
#BIG THETA
#-Theta(n log n)


#2. Pseudocode untuk bubble sort
#function bubbleSort(array):
# n = length of array
# for i from 0 to n-1:
#     for j from 0 to n-i-2:
#         if array[j] > array[j+1]:
#             swap array[j] and array[j+1]
# return array
#--------------------KOMPLEKSITAS-------------------------------------
#BIG O
#O(n^2) karena terdapat dua nested loop
#BIG THETA
#Theta(n^2) karna setiap elemen dibandingkan dengan setiap elemen lainnya.


import random
import time

# Merge Sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

x = [random.randint(1, 1000) for _ in range(100)]

# Time for Merge Sort
start_time = time.time()
sorted_merge = merge_sort(x.copy())
merge_sort_time = time.time() - start_time

# Time for Bubble Sort
start_time = time.time()
sorted_bubble = bubble_sort(x.copy())
bubble_sort_time = time.time() - start_time

print("Original Array:", x)
print("\nSorted Array using Merge Sort:", sorted_merge)
print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

print("\nSorted Array using Bubble Sort:", sorted_bubble)
print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")


