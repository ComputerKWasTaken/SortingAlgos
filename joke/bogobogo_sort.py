import matplotlib.pyplot as plt
import random
from typing import List

def is_sorted(arr: List[int]) -> bool:
    """ Check if the array is sorted. """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogoSort(arr: List[int]) -> None:
    """ Bogo Sort algorithm """
    while not is_sorted(arr):
        random.shuffle(arr)

def bogobogoSort(arr: List[int], ax=None) -> None:
    """ Implements the BogoBogo Sort algorithm with visualization. """
    passNum = 0
    while not is_sorted(arr):
        for i in range(len(arr)):
            sub_array = arr[:i + 1]
            bogoSort(sub_array)
            arr[:i + 1] = sub_array  # Update the original array
            visualize(arr, passNum, i, i, ax)
            passNum += 1
        random.shuffle(arr)
        visualize(arr, passNum, -1, -1, ax)
        passNum += 1

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """ Updates the matplotlib bar graph for visualization. """
    ax.clear()
    barColors = ['blue'] * len(arr)
    if selectedIndex >= 0:
        barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'BogoBogo Sort Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
