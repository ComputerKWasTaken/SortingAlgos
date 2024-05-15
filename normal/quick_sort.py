import matplotlib.pyplot as plt
from typing import List

def quickSort(arr: List[int], low: int, high: int, passNum: int = 0, ax=None):
    """ Implements the quick sort algorithm with visualization. """
    if low < high:
        pi = partition(arr, low, high, passNum, ax)
        quickSort(arr, low, pi - 1, passNum + 1, ax)
        quickSort(arr, pi + 1, high, passNum + 1, ax)

def partition(arr: List[int], low: int, high: int, passNum: int, ax):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            visualize(arr, passNum, i, j, ax)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualize(arr, passNum, i + 1, high, ax)
    return i + 1

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Sorting Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
