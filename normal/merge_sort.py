import matplotlib.pyplot as plt
from typing import List

def insertion_sort(arr: List[int], left: int, right: int, ax=None):
    """Insertion sort for small subarrays"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if ax:
            visualize(arr, 0, j + 1, i, ax)

def merge_in_place(arr: List[int], l: int, m: int, r: int, ax=None):
    """In-place merging to reduce memory usage"""
    # If the direct merge is already sorted
    if arr[m] <= arr[m + 1]:
        return

    start2 = m + 1
    while l <= m and start2 <= r:
        if arr[l] <= arr[start2]:
            l += 1
        else:
            value = arr[start2]
            index = start2
            
            # Shift all elements between l and start2 right by 1
            while index != l:
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[l] = value
            l += 1
            m += 1
            start2 += 1
            
            if ax:
                visualize(arr, 0, l-1, start2-1, ax)

def mergeSort(arr: List[int], l: int, r: int, passNum: int = 0, ax=None):
    """Optimized merge sort with insertion sort for small arrays"""
    if r - l <= 10:  # Use insertion sort for small arrays
        insertion_sort(arr, l, r, ax)
        return
        
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m, passNum + 1, ax)
        mergeSort(arr, m + 1, r, passNum + 1, ax)
        merge_in_place(arr, l, m, r, ax)

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Sorting Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
