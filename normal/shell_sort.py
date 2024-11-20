import matplotlib.pyplot as plt
from typing import List

def shellSort(arr: List[int], ax=None):
    """ Applies a shell sort algorithm, visualizing each step. """
    if not arr:
        return arr
        
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                if ax:
                    visualize(arr, gap, i, j, ax)
            arr[j] = temp
            if ax:
                visualize(arr, gap, i, j, ax)
        gap //= 2

    return arr

def visualize(arr: List[int], gap: int, currentIndex: int, swapIndex: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[currentIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Gap: {gap}, Current Index: {currentIndex}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
