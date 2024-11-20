import matplotlib.pyplot as plt
import math
from typing import List
from normal.heap_sort import heapSort

def insertion_sort(arr: List[int], start: int, end: int, passNum: int, ax=None):
    """Optimized insertion sort for small arrays"""
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if ax:
                visualize(arr, passNum, j + 1, i, ax)
        arr[j + 1] = key
        if ax:
            visualize(arr, passNum, j + 1, i, ax)

def partition(arr: List[int], low: int, high: int, passNum: int, ax=None):
    """Optimized partition with simple pivot selection"""
    # Use middle element as pivot to avoid worst case for sorted arrays
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                if ax:
                    visualize(arr, passNum, i, j, ax)
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if ax:
        visualize(arr, passNum, i + 1, high, ax)
    return i + 1

def introSort(arr: List[int], ax=None):
    """Main Introsort function"""
    if not arr:
        return arr
    
    max_depth = 2 * int(math.log2(len(arr)))
    _introSort(arr, 0, len(arr) - 1, max_depth, 0, ax)
    return arr

def _introSort(arr: List[int], start: int, end: int, max_depth: int, passNum: int, ax=None):
    """Recursive Introsort helper"""
    size = end - start + 1
    
    # Use insertion sort for small arrays
    if size <= 16:
        insertion_sort(arr, start, end, passNum, ax)
        return
    
    # If recursion too deep, switch to heapsort
    if max_depth <= 0:
        if ax:
            visualize(arr, passNum, start, end, ax)
        heapSort(arr[start:end + 1], ax)
        return
    
    # Otherwise, use quicksort partitioning
    pivot = partition(arr, start, end, passNum, ax)
    
    # Recurse on smaller partition first
    if pivot - start < end - pivot:
        _introSort(arr, start, pivot - 1, max_depth - 1, passNum + 1, ax)
        _introSort(arr, pivot + 1, end, max_depth - 1, passNum + 1, ax)
    else:
        _introSort(arr, pivot + 1, end, max_depth - 1, passNum + 1, ax)
        _introSort(arr, start, pivot - 1, max_depth - 1, passNum + 1, ax)

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    if ax is None:
        return
        
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Intro Sort Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
