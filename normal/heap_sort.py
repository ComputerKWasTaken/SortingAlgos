import matplotlib.pyplot as plt
from typing import List

def heapify(arr: List[int], n: int, i: int, passNum: int, ax):
    """Heapify subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        visualize(arr, passNum, i, largest, ax)
        heapify(arr, n, largest, passNum, ax)

def heapSort(arr: List[int], ax=None):
    """Implements the heap sort algorithm with visualization."""
    n = len(arr)
    passNum = 0

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, passNum, ax)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        visualize(arr, passNum, 0, i, ax)
        heapify(arr, i, 0, passNum, ax)
        passNum += 1

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Heap Sort Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
