import matplotlib.pyplot as plt
from typing import List

def mergeSort(arr: List[int], l: int, r: int, passNum: int = 0, ax=None):
    """ Implements the merge sort algorithm with visualization. """
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m, passNum + 1, ax)
        mergeSort(arr, m + 1, r, passNum + 1, ax)
        merge(arr, l, m, r, passNum, ax)

def merge(arr: List[int], l: int, m: int, r: int, passNum: int, ax):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        visualize(arr, passNum, k, k, ax)
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        visualize(arr, passNum, k, k, ax)
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        visualize(arr, passNum, k, k, ax)
        k += 1

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
