import matplotlib.pyplot as plt
from typing import List

def cocktailShakerSort(arr: List[int], ax=None):
    """ Implements the cocktail shaker sort algorithm with visualization. """
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    passNum = 0

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize(arr, passNum, i, i + 1, ax)
        
        if not swapped:
            break

        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize(arr, passNum, i, i, ax)
        
        start += 1
        passNum += 1

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
