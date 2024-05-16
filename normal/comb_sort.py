import matplotlib.pyplot as plt
from typing import List

def combSort(arr: List[int], ax=None):
    """ Applies a comb sort algorithm, visualizing each step. """
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))  # Minimum gap is 1
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
                visualize(arr, gap, i, ax)

    return arr

def visualize(arr: List[int], gap: int, currentIndex: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[currentIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Gap: {gap}, Current Index: {currentIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
