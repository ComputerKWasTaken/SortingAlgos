import matplotlib.pyplot as plt
import math
from typing import List
from normal.heap_sort import heapify

def introSort(arr: List[int], ax=None):
    """Implements the intro sort algorithm with visualization."""
    max_depth = 2 * int(math.log2(len(arr)))
    _introSort(arr, 0, len(arr) - 1, max_depth, 0, ax)

def _introSort(arr: List[int], start: int, end: int, max_depth: int, passNum: int, ax):
    """Helper function for intro sort."""
    if start < end:
        if max_depth == 0:
            heapSort(arr, start, end, ax, passNum)
        else:
            p = partition(arr, start, end, passNum, ax)
            _introSort(arr, start, p - 1, max_depth - 1, passNum, ax)
            _introSort(arr, p + 1, end, max_depth - 1, passNum, ax)

def heapSort(arr: List[int], start: int, end: int, ax, passNum):
    """Heap sort used by intro sort."""
    n = end - start + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i + start, passNum, ax)
    for i in range(n - 1, 0, -1):
        arr[start + i], arr[start] = arr[start], arr[start + i]
        visualize(arr, passNum, start + i, start, ax)
        heapify(arr, i, start, passNum, ax)
        passNum += 1

def partition(arr: List[int], low: int, high: int, passNum: int, ax):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            visualize(arr, passNum, i, j, ax)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualize(arr, passNum, i + 1, high, ax)
    return i + 1

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Intro Sort Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
