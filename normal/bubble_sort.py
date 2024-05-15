import matplotlib.pyplot as plt
from typing import List

def bubbleSortRecursive(arr: List[int], n: int, passNum: int = 0, ax=None):
    """ Recursively applies a bubble sort algorithm, visualizing each step. """
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            visualize(arr, passNum, i, i + 1, ax)
    
    return bubbleSortRecursive(arr, n - 1, passNum + 1, ax)

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
