import matplotlib.pyplot as plt
from typing import List

def sift_down(arr: List[int], start: int, end: int, passNum: int, ax=None):
    """Optimized sift-down operation using temp variable to reduce swaps"""
    root = start
    temp = arr[root]
    
    while True:
        child = 2 * root + 1
        if child > end:
            break
            
        # Find the larger child
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
            
        # If largest child is larger than root, move it up
        if arr[child] > temp:
            arr[root] = arr[child]
            if ax:
                visualize(arr, passNum, root, child, ax)
            root = child
        else:
            break
    
    arr[root] = temp
    if ax:
        visualize(arr, passNum, root, start, ax)

def heapify(arr: List[int], n: int, i: int, passNum: int, ax=None):
    """Build max heap using optimized sift-down"""
    sift_down(arr, i, n - 1, passNum, ax)

def heapSort(arr: List[int], ax=None):
    """Optimized heap sort implementation"""
    if not arr:
        return arr
        
    n = len(arr)
    passNum = 0
    
    # Build heap (rearrange array) in O(n) time
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, passNum, ax)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        if ax:
            visualize(arr, passNum, 0, i, ax)
        passNum += 1
        
        # Call heapify on the reduced heap
        sift_down(arr, 0, i - 1, passNum, ax)
    
    return arr

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
