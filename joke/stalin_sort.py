import matplotlib.pyplot as plt
from typing import List

def stalinSort(arr: List[int], ax=None):
    """ Implements the Stalin sort algorithm with visualization. """
    passNum = 0
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            arr.pop(i)
        else:
            i += 1
        visualize(arr, passNum, ax)
        passNum += 1

def visualize(arr: List[int], passNum: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Stalin Sort Pass: {passNum}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
