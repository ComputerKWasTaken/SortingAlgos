import matplotlib.pyplot as plt
import random
from typing import List

def is_sorted(arr: List[int]) -> bool:
    """ Check if the array is sorted. """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogoSort(arr: List[int], ax=None):
    """ Implements the bogo sort algorithm with visualization. """
    passNum = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        visualize(arr, passNum, ax)
        passNum += 1

def visualize(arr: List[int], passNum: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Bogo Sort Pass: {passNum}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
