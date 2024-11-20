import matplotlib.pyplot as plt
from typing import List

def insertion_sort(arr: List[int], low: int, high: int, ax=None):
    """Insertion sort for small subarrays"""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if ax:
            visualize(arr, 0, j + 1, i, ax)

def median_of_three(arr: List[int], low: int, high: int):
    """Choose median of first, middle, and last elements as pivot"""
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def partition(arr: List[int], low: int, high: int, ax=None):
    """Improved partition using median-of-three pivot selection"""
    if high - low > 10:  # Only use median-of-three for larger arrays
        pivot_idx = median_of_three(arr, low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if ax:
                visualize(arr, 0, i, j, ax)
                
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if ax:
        visualize(arr, 0, i + 1, high, ax)
    return i + 1

def quickSort(arr: List[int], low: int, high: int, passNum: int = 0, ax=None):
    """Optimized quicksort with tail-call elimination and insertion sort for small arrays"""
    while low < high:
        if high - low + 1 < 10:  # Use insertion sort for small arrays
            insertion_sort(arr, low, high, ax)
            break
        
        pivot = partition(arr, low, high, ax)
        
        # Tail call optimization: always recurse on smaller partition
        if pivot - low < high - pivot:
            quickSort(arr, low, pivot - 1, passNum + 1, ax)
            low = pivot + 1
        else:
            quickSort(arr, pivot + 1, high, passNum + 1, ax)
            high = pivot - 1

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
